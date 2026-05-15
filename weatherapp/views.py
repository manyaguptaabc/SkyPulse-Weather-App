# weatherapp/views.py
import requests
import logging
from django.http import JsonResponse
from concurrent.futures import ThreadPoolExecutor

# Set up logging
logger = logging.getLogger(__name__)

# Your OpenWeatherMap API key
API_KEY = '809e714706013f07be1053d724d47824'

# List of 10 cities
CITIES = ["Delhi","Mumbai","Bangalore","Chennai","Kolkata",
          "Hyderabad","Pune","Ahmedabad","Jaipur","Lucknow"]

# Function to fetch weather for a single city
def fetch_city_weather(city):
    try:
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}",
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
        return {
            "city": city,
            "temp": round(data['main']['temp'], 2),
            "description": data['weather'][0]['description']
        }
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch weather for {city}: {e}")
        return {
            "city": city,
            "temp": None,
            "description": "Data not available"
        }

# View to fetch weather for all cities
def get_weather(request):
    with ThreadPoolExecutor() as executor:
        weather_data = list(executor.map(fetch_city_weather, CITIES))
    return JsonResponse({"weather": weather_data})
