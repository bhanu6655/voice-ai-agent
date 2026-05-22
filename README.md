# 🎤 Real-Time Voice AI Appointment Agent

A multilingual AI-powered Voice Appointment Assistant that allows users to interact using voice conversations to:

- Book appointments
- Cancel appointments
- Reschedule appointments

The system uses:

- FastAPI
- Groq LLM
- Browser Speech Recognition
- gTTS
- SQLite

Supported Languages:

- English
- Hindi
- Tamil

---

# 🚀 Features

✅ Real-time voice interaction  
✅ AI-powered appointment assistant  
✅ Groq LLM integration  
✅ Multilingual support  
✅ Voice responses using gTTS  
✅ Appointment booking system  
✅ Context memory  
✅ Lightweight deployment-ready architecture  
✅ Render deployment support  

---

# 🏗️ Tech Stack

| Technology | Purpose |
|---|---|
| FastAPI | Backend Framework |
| Groq API | AI Responses |
| gTTS | Text-to-Speech |
| SQLite | Database |
| HTML/CSS/JavaScript | Frontend |
| Browser Speech Recognition | Speech-to-Text |

---

# 📁 Project Structure

```text
voice-ai-agent/
│
├── app.py
├── appointments.db
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── script.js
│
├── audio/
│   ├── input.wav
│   └── output.mp3
│
├── services/
│   ├── stt.py
│   ├── tts.py
│   ├── agent.py
│   ├── db.py
│   └── memory.py



1. Clone Repository
git clone https://github.com/your-username/voice-ai-agent.git

cd voice-ai-agent
2. Create Virtual Environment
Windows
python -m venv venv

venv\Scripts\activate
Linux/Mac
python3 -m venv venv

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
📦 requirements.txt
fastapi
uvicorn
jinja2
python-multipart
gtts
groq
python-dotenv
sqlalchemy
🔑 Environment Variables

Create a .env file in the root folder.

GROQ_API_KEY=your_groq_api_key

Get API Key from:

https://console.groq.com/keys

▶️ Run Project
uvicorn app:app --reload

Open browser:

http://127.0.0.1:8000
🎙️ How It Works
User Voice
    ↓
Browser Speech Recognition
    ↓
FastAPI Backend
    ↓
Groq AI
    ↓
Appointment Logic
    ↓
gTTS Voice Response
    ↓
User Hears Reply
🤖 AI Features

The AI assistant can:

Understand appointment requests
Handle multilingual conversations
Generate natural responses
Maintain context memory
Manage appointment workflows
🌍 Supported Languages
Language	Support
English	✅
Hindi	✅
Tamil	✅
📡 API Endpoint
POST /voice
Request
{
  "text": "Book dentist appointment tomorrow"
}
Response

Returns generated voice audio response.

🧠 Context Memory

Conversation history is stored temporarily during runtime.

Example:

conversation_memory = []

This helps maintain conversational flow.

🗄️ Database

SQLite database stores appointment information.

Appointment Table
Column	Type
id	INTEGER
patient_name	TEXT
doctor_name	TEXT
appointment_date	TEXT
status	TEXT
☁️ Deployment

This project can be deployed on:

Render
Railway
VPS
Docker
🚀 Deploy on Render
Build Command
pip install -r requirements.txt
Start Command
uvicorn app:app --host 0.0.0.0 --port 10000
Add Environment Variable in Render
KEY	VALUE
GROQ_API_KEY	your_api_key
📸 Demo Features

✅ Voice Input
✅ AI Conversation
✅ Voice Output
✅ Appointment Booking
✅ Multilingual AI
✅ Context Memory

🔮 Future Enhancements
Real-time streaming
Doctor availability checking
Authentication system
Twilio phone call integration
Redis memory
PostgreSQL database
WebSockets
ElevenLabs voices
Vector database memory
│
└── utils/
    └── language.py
