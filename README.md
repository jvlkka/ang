# VoiceBot Web Application

A modern web application featuring user authentication and AI-powered voice interaction capabilities.

## Project Structure

```
MaturaProjekt/
├── backend/              # Flask backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models/
│   │   ├── routes/
│   │   └── config.py
│   └── run.py
├── frontend/            # React frontend
│   ├── public/
│   └── src/
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Setup Instructions

### Backend Setup
1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in `.env`

4. Run the backend:
   ```bash
   python backend/run.py
   ```

### Frontend Setup
1. Install Node.js dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm start
   ```

## Features
- User Authentication (Login/Register)
- Secure Password Handling
- JWT Token-based Authentication
- VoiceBot Integration (Coming Soon)

## Technologies Used
- Backend: Flask, SQLAlchemy, PostgreSQL
- Frontend: React, Material-UI
- Authentication: JWT
- API: RESTful Architecture
