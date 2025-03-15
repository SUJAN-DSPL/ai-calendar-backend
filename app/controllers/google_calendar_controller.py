import cherrypy
from marshmallow import ValidationError
from app.services.google_auth_service import GoogleAuthService
from googleapiclient.discovery import build
from app.schemas.create_meeting_schema import CreateMeetingSchema
from google.auth.exceptions import GoogleAuthError
from app.tools.auth import use_auth

use_auth()

class GoogleCalendarController:
    
    def __init__(self):
        self.google_auth_service = GoogleAuthService()
    
    @cherrypy.expose("meetings")
    @cherrypy.tools.json_out()
    @cherrypy.tools.allow(methods=["GET"])
    @cherrypy.tools.auth()
    def fetch_meetings(self, **param):
        date = param['date']
        user = cherrypy.request.user
        credentials =  self.google_auth_service.get_user_credentials(user['id']);
        service = build("calendar", "v3", credentials=credentials)
        start_time = f"{date}T00:00:00Z"
        end_time = f"{date}T23:59:59Z"
        events_result = service.events().list(
            calendarId="primary", timeMin=start_time, timeMax=end_time, singleEvents=True, orderBy="startTime"
        ).execute()
        return events_result.get("items", [])
    
    @cherrypy.expose("create_meeting")
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    @cherrypy.tools.allow(methods=["POST"])
    def create_meeting(self):
        data = cherrypy.request.json
        schema = CreateMeetingSchema()
        
        try:
            data = schema.load(data)
        except ValidationError as err:
            cherrypy.response.status = 400
            return {"error": err.messages}

        event = {
            "summary": data["summary"],
            "description": data["description"],
            "start": {"dateTime": data["start_time"], "timeZone": data['time_zone']},
            "end": {"dateTime": data["end_time"], "timeZone": data['time_zone']},
            "attendees": [{"email": email} for email in data["attendees"]],
            "reminders": {
                    "useDefault": False,
                    "overrides": [
                        {"method": "email", "minutes": 30},  
                        {"method": "popup", "minutes": 10},  
                    ],
            },
        }
        
        if data["video_conference"] == True:
            event["conferenceData"] = {
                "createRequest": {
                    "requestId": "meeting-" + data["summary"],
                    "conferenceSolutionKey": {"type": "hangoutsMeet"}
                }
            }

        credentials =  self.google_auth_service.get_user_credentials(1);
        service = build("calendar", "v3", credentials=credentials)
        event = service.events().insert(
             calendarId="primary",
             body=event,
             sendUpdates="all", 
             conferenceDataVersion=1  
        ).execute()

        return {
            "event_id": event["id"],
            "meet_link": event["conferenceData"]["entryPoints"][0]["uri"] if data["video_conference"] else None,
            "status": "created",
            "attendees": data["attendees"]
        }
        
    @cherrypy.expose("delete_meeting")
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    @cherrypy.tools.allow(methods=["POST"])
    def delete_meeting(self):
       
        try:
            credentials = self.google_auth_service.get_user_credentials(1) 
            service = build("calendar", "v3", credentials=credentials)

            data = cherrypy.request.json
            event_id = data.get("event_id")
            
            if not event_id:
                return {"error": "event_id is required"}

            service.events().delete(calendarId="primary", eventId=event_id).execute()
            
            return {"status": "success", "message": "Meeting deleted successfully"}

        except GoogleAuthError as auth_error:
            return {"error": "Authentication failed", "details": str(auth_error)}

        except Exception as e:
            return {"error": "Failed to delete meeting", "details": str(e)}