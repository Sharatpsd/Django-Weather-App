# 🌤️ Django Weather App  
### (Django + REST API + Frontend)

🔗 **Live Demo:** https://weather-c5n7.onrender.com/

A simple and practical **Django-based weather application** that fetches **real-time weather data** for any city using a third-party Weather API.  
This project demonstrates **Django fundamentals, REST API integration, and frontend rendering** in a clean full-stack workflow.

---

## 🖼️ Application Screenshots

Below are real screenshots of the application interface and functionality:


<p align="center">
  <img src="https://drive.google.com/uc?id=1igWXvf3PoGHn7iHAWNHdhZTlYScJJQ_0" width="600"/>
</p>

<p align="center">
  <img src="https://drive.google.com/uc?id=19xgyLajiiKIn2Q8Vrv4R6TEAJ757ufT_" width="600"/>
</p>

---

## 📌 Key Features

- 🌍 Search current weather by **city name**
- 🔌 Fetches **real-time data** from a Weather REST API
- 🌡️ Displays temperature, humidity, and weather condition
- ⚠️ Handles invalid city names gracefully
- 🎨 Clean and simple user interface
- 🚀 Live deployed application

---

## 🧠 What This Project Demonstrates

- Django project & app structure  
- URL → View → Template workflow  
- REST API consumption using `requests`  
- JSON response parsing  
- Secure handling of API keys using environment variables  
- Basic deployment experience  

> This is a **beginner to intermediate level Django project**.

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework  
- **Frontend:** HTML, CSS, Django Templates  
- **API:** OpenWeatherMap (or similar weather API)  
- **Database:** SQLite (development)  
- **Deployment:** Render  
- **Language:** Python 3.x  

---

## ⚙️ Local Setup & Installation

```bash
# Clone the repository
git clone https://github.com/Sharatpsd/Django-Weather-App.git
cd Django-Weather-App

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run development server
python manage.py runserver

