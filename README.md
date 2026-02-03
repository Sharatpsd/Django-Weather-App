# 🌤️ Django Weather App

**Modern Full-Stack Weather Application**  
Real-time weather dashboard built with **Django**, **Django REST Framework**, and clean frontend templating.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2+-094067?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.14+-red)](https://www.django-rest-framework.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-46a2f1?logo=render)](https://render.com)

🔗 **Live Demo:** [https://weather-c5n7.onrender.com/](https://weather-c5n7.onrender.com/)

Clean, responsive weather application that fetches real-time weather data using the **OpenWeatherMap API**.  
Great starter project demonstrating proper **Django structure**, **REST API consumption**, **environment configuration**, **error handling**, and **production-ready deployment practices**.

## 📸 Screenshots

<p align="center">
  <img src="https://drive.google.com/uc?id=1HbvnCTmbw3SxwQUqyreQDG1pYnDuW6c5" width="48%" alt="Home - Search"/>
  <img src="https://drive.google.com/uc?id=1H2v9Uud1FJX8pJU5oPtaqFS3_lGszvnk" width="48%" alt="Weather Result"/>
</p>

<p align="center">
  <img src="https://drive.google.com/uc?id=1Kv9oxkqUhJjy91kMTMpRp6TUYogGzPEL" width="48%" alt="Error Handling"/>
  <img src="https://drive.google.com/uc?id=10kULKg5AkxL0LDA1iVb1t8-D8DXG7tkU" width="48%" alt="Responsive Design"/>
</p>

<p align="center">
  <img src="https://drive.google.com/uc?id=14YzIb_xdjjAmde4yg7svmFzUMXoeP6eh" width="60%" alt="Mobile View"/>
</p>

> Tip: All screenshots were taken from the live deployment.

## ✨ Features

- 🔍 Search current weather by **city name** (supports international cities)
- 🌡️ Real-time data: temperature (°C/°F), feels like, humidity, wind, condition + icon
- ⚡ Fast API integration using `requests` library
- 🛡️ Graceful error handling (invalid city, API failures, rate limits)
- 🎨 Clean, responsive UI (mobile-friendly)
- 🔐 Secure API key handling via `.env` / environment variables
- 🚀 Production-ready deployment configuration (Render, gunicorn, static files)
- 📡 RESTful endpoint `/api/weather/<city>/` (JSON response)

## 🏗️ Tech Stack

| Layer         | Technology                            | Purpose                              |
|---------------|---------------------------------------|--------------------------------------|
| Backend       | Django 4.x                            | Web framework                        |
| API           | Django REST Framework                 | REST API layer (optional)            |
| HTTP Client   | requests                              | Weather API consumption              |
| Frontend      | Django Templates + HTML5 + CSS3       | Server-side rendering                |
| Styling       | Custom CSS / Bootstrap (optional)     | Responsive layout                    |
| API           | OpenWeatherMap                        | Real-time weather data               |
| Database      | SQLite (dev) • PostgreSQL (prod rec.) | Data persistence                     |
| Deployment    | Render / Heroku-compatible            | Free / low-cost hosting              |
| Environment   | python-dotenv                         | Secure configuration                 |

## ⚡ Quick Start (Local Development)

```bash
# 1. Clone the repository
git clone https://github.com/Sharatpsd/Django-Weather-App.git
cd Django-Weather-App

# 2. Create & activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file (very important!)
cp .env.example .env    # if .env.example exists — otherwise create manually

# Edit .env and add your OpenWeatherMap key:
# SECRET_KEY=your-very-long-random-django-secret-key
# DEBUG=True
# ALLOWED_HOSTS=localhost,127.0.0.1

# 5. Apply migrations & create superuser (optional)
python manage.py migrate
python manage.py createsuperuser    # optional

# 6. Run the development server
python manage.py runserver

