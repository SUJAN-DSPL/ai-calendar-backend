# AI Calendar

![AI Calendar](https://uniconcloud.com/assets/images/unicon-cloud-logo.png)

## 🚀 Overview
AI Calendar automates calendar workflows using AI-powered scheduling and management. This project integrates **LangChain**, **CherryPy**, **SQLAlchemy**, **Alembic**, and **Google API** to create, manage, and optimize calendar events efficiently.

## 🛠️ Technologies Used
- **LangChain** - AI-powered workflow automation
- **CherryPy** - Lightweight Python web framework
- **SQLAlchemy** - Database ORM for structured data
- **Alembic** - Database migration tool
- **Google API** - Integration with Google Calendar

## 📌 Features
✅ AI-assisted scheduling of meetings  
✅ Fetching meetings from Google Calendar  
✅ Managing events with natural language input  
✅ Automatic time optimization for scheduling  
✅ Seamless database integration  

---

## 📦 Installation Guide
Follow these steps to set up and run the AI Calendar project.

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/ai-calendar.git
cd ai-calendar
```

### 2️⃣ Set Up Virtual Environment
#### 🔹 Windows
```sh
python -m venv venv
venv\Scripts\activate
```
#### 🔹 macOS & Linux
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file and set up the following:
```
DB_URL=<your-database-url>
GOOGLE_CLIENT_ID=<your-google-client-id>
GOOGLE_CLIENT_SECRET=<your-google-client-secret>
GOOGLE_API_KEY=<your-google-api-key>
```

### 5️⃣ Apply Database Migrations
```sh
alembic upgrade head
```

### 6️⃣ Run the Application
```sh
python main.py
```

---

## 📖 Usage
- Start the application and authenticate with your Google account.
- Use the AI assistant to schedule, fetch, and manage calendar events.
- API endpoints available for integration with other services.

