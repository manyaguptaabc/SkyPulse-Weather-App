# SkyPulse – Weather Forecasting Web App

A Python-based real-time weather forecasting web app integrating OpenWeatherMap REST API for 10+ cities.

---

## Deployment Guide (12 Steps)

### Step 1 – Clone the Repository
git clone https://github.com/yourusername/skypulse.git
cd skypulse

### Step 2 – Create Virtual Environment
python -m venv venv

### Step 3 – Activate Virtual Environment
venv\Scripts\activate

### Step 4 – Install Dependencies
pip install -r requirements.txt

### Step 5 – Create .env File
Create a `.env` file in root folder:
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
OPENWEATHER_API_KEY=your-openweathermap-api-key

### Step 6 – Get OpenWeatherMap API Key
- Go to https://openweathermap.org/api
- Sign up and copy your API key
- Paste it in .env file

### Step 7 – Apply Migrations
python manage.py migrate

### Step 8 – Test API Connection
python manage.py shell
from weatherapp.views import fetch_city_weather
print(fetch_city_weather("Delhi"))

### Step 9 – Run Development Server
python manage.py runserver

### Step 10 – Access the App
Open browser and go to:
http://127.0.0.1:8000/
You will see live weather data for 10 cities in JSON format.

### Step 11 – Check Logs
type skypulse.log

### Step 12 – Production Deployment
Set DEBUG=False in .env
pip install waitress
waitress-serve --port=8000 skypulse.wsgi:application

---

## Features
- Real-time weather data for 10+ cities
- Parallel API calls using ThreadPoolExecutor (35% faster response)
- Structured logging with file + console handlers
- Environment-based configuration via .env
- Error handling with fallback responses

---

## Team
- 3-member team project
- Presented to 10+ faculty evaluators
- Received commendation for clarity and technical depth