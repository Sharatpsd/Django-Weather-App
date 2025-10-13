# 🌤️ Django Weather App (REST API + Frontend)
##### live link ----https://weather-c5n7.onrender.com/

> A sleek, powerful weather application built with **Django** and **Django REST Framework**, featuring a dynamic frontend to display current weather for user-specified cities.

---

## Welcome & Preview

Below are screenshots / frontpage images of the application to give you an idea of the UI & design:

<p align="center">
  <img src="https://drive.google.com/uc?id=1HbvnCTmbw3SxwQUqyreQDG1pYnDuW6c5" alt="Frontpage Image 1" width="600"/>
  <img src="https://drive.google.com/uc?id=1H2v9Uud1FJX8pJU5oPtaqFS3_lGszvnk" alt="Frontpage Image 2" width="600"/>
</p>
<p align="center">
  <img src="https://drive.google.com/uc?id=1Kv9oxkqUhJjy91kMTMpRp6TUYogGzPEL" alt="Frontpage Image 3" width="600"/>
  <img src="https://drive.google.com/uc?id=10kULKg5AkxL0LDA1iVb1t8-D8DXG7tkU" alt="Frontpage Image 4" width="600"/>
</p>
<p align="center">
  <img src="https://drive.google.com/uc?id=14YzIb_xdjjAmde4yg7svmFzUMXoeP6eh" alt="Frontpage Image 5" width="600"/>
</p>

---

## 📋 Table of Contents

1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Setup & Installation](#setup--installation)  
4. [Configuration](#configuration)  
5. [Usage](#usage)  
6. [API Endpoints](#api-endpoints)  
7. [Testing](#testing)  
8. [Deployment](#deployment)  
9. [Contributing](#contributing)  
10. [Contact & License](#contact--license)

---

## ✅ Features

- Fetch current weather by **city name** via REST API  
- JSON formatted responses with temperature, humidity, weather description, etc.  
- Friendly frontend UI: search box, display weather, responsive design  
- Error handling (invalid city, network issues)  
- Optional enhancements: favorites, multiple cities, caching  

---

## 🛠️ Tech Stack

| Layer         | Technologies |
|----------------|----------------|
| **Backend**    | Django, Django REST Framework |
| **Frontend**   | Django Templates / HTML / CSS / JS (or optionally React/Vue/other) |
| **Data Source**| OpenWeatherMap API (or similar) |
| **Database**   | SQLite (default), easily configurable to PostgreSQL/MySQL |
| **Tools**      | Git, Python 3.x, REST API, virtualenv / venv |

---

## ⚙️ Setup & Installation

These steps assume you’re starting fresh in a local dev environment.

```bash
# 1. Clone the repository
git clone https://github.com/Sharatpsd/Django-Weather-App.git

# 2. Change into project directory
cd Django-Weather-App

# 3. Create virtual environment (recommended)
python3 -m venv venv
# For Windows:
# venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Apply database migrations
python manage.py migrate
🔐 Configuration
Copy the .env.example (if provided) to .env, or set environment variables:

ini
Copy code
WEATHER_API_KEY=your_openweathermap_api_key
SECRET_KEY=your_django_secret_key
DEBUG=True   # Turn to False for production
ALLOWED_HOSTS=localhost,127.0.0.1
Ensure static files settings are correct in production (STATIC_ROOT, etc.)

🚀 Usage
bash
Copy code
# Activate virtualenv (if not already)
source venv/bin/activate

# Run development server
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser. On the front page you can:

Enter a city name to get current weather

See error messages if city not found or something fails

Also test the REST API (see below).

📡 API Endpoints
Endpoint	Method	Description
/api/weather/?city=<cityname>	GET	Returns current weather data for given city
/api/cities/	GET/POST	(Optional) List added cities / Add a new city
/api/weather/<city_id>/	GET	(Optional) Get weather for city by internal ID

Note: Replace <cityname> or <city_id> appropriately.

🧪 Testing
If you’ve written tests, run:

bash
Copy code
python manage.py test
Make sure:

Tests cover successful API fetches, error responses

Frontend displays correct data and handles errors gracefully

🌐 Deployment
To deploy this app to production:

Ensure DEBUG=False

Use a production-ready database (e.g. PostgreSQL)

Use a WSGI server (Gunicorn, uWSGI, etc.)

Collect static files:

bash
Copy code
python manage.py collectstatic
Set up allowed hosts, secure settings, environment variables

(Optional) Use HTTPS, reverse proxy (e.g. nginx), domain name

🤝 Contributing
Your contributions are very welcome! Here’s how to help:

Fork the repo

Create a new branch (git checkout -b feature/my-feature)

Make changes & write tests

Open a Pull Request with a clear description

Ensure code follows style guidelines (PEP8, etc.)

📞 Contact & License
GitHub: Sharatpsd

Email: sharatacharjee6@gmail.com


