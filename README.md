# NIVO Education

NIVO Education is an AI-powered education and career guidance platform designed to help students and young professionals explore their academic and career options.

The project combines a Wix frontend with a custom Flask REST API, AI-powered guidance, lead collection, and a protected lead management dashboard.

## Features

- AI-powered education and career guidance
- Responsive Wix frontend
- Custom Flask REST API
- Groq-powered AI integration
- Student enquiry and lead collection
- SQLite database
- Protected lead dashboard
- Admin authentication for lead access
- Public backend deployment with Render

## How It Works

1. Users visit the NIVO Education website.
2. They can ask NIVO AI questions about education and career options.
3. The Wix frontend sends messages to the Flask API.
4. The backend communicates with the AI service and returns the response.
5. Users can submit their name, phone number, and an optional message through the enquiry form.
6. Enquiries are stored in SQLite.
7. Authorised users can view submitted leads through the protected dashboard.

## Tech Stack

### Frontend
- Wix
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask
- Gunicorn
- REST API

### AI
- Groq API

### Database
- SQLite

### Deployment
- Render
- GitHub

## API Endpoints

### Health Check

`GET /health`

Checks whether the NIVO backend is running.

### AI Chat

`POST /api/sohbet`

Example request:

```json
{
  "mesaj": "I want to study Computer Science. What should I consider?"
}
```

### Submit Lead

`POST /api/leads`

Example request:

```json
{
  "isim": "Test Student",
  "telefon": "07111111111",
  "mesaj": "I am interested in studying Computer Science."
}
```

### View Leads

`GET /api/leads`

This endpoint is protected and requires the admin password through the `X-Admin-Password` request header.

## Security

Sensitive configuration such as API keys and admin credentials is stored using environment variables and is not committed to the repository.

The `.env` file, virtual environment, local database files, and other development files are excluded through `.gitignore`.

## Environment Variables

The application uses environment variables including:

```text
GROQ_API_KEY
ADMIN_PASSWORD
SECRET_KEY
```

Do not commit real environment variable values to the repository.

## Local Development

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file containing the required environment variables.

Run the application:

```bash
python3 run.py
```

The development server will run locally at:

`http://127.0.0.1:5000`

## Production

The Flask backend is deployed as a Render Web Service using:

```text
Build Command: pip install -r requirements.txt
Start Command: gunicorn run:app
```

## Live Project

Frontend:

`https://altugyamakk.wixsite.com/nivo-education`

Backend:

`https://nivo-education.onrender.com`

Health Check:

`https://nivo-education.onrender.com/health`

## Project Structure

```text
nivo-education/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── ...
├── config.py
├── requirements.txt
├── run.py
├── .gitignore
└── README.md
```

## Current MVP Scope

NIVO Education currently focuses on:

- AI-powered education and career guidance
- Student enquiry collection
- Lead management through a protected dashboard

The current deployment uses SQLite for the MVP. Persistent production-scale database infrastructure can be introduced in a future version.

## Future Improvements

Potential future developments include:

- PostgreSQL database
- Expanded admin dashboard
- Lead status management
- University and course data integrations
- Multilingual support
- User accounts
- Analytics
- Custom domain
- Additional AI guidance capabilities

## Disclaimer

NIVO AI provides general education and career guidance. Information such as university entry requirements, tuition fees, visa rules, scholarships, and deadlines may change and should always be verified with the relevant university or official authority.

## Author

**Altug Yamak**

*An AI-powered platform for smarter education and career decisions.*
