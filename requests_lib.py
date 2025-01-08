# Using weather api to fetch weather data.
import os
import requests
from dotenv import load_dotenv

# Load environment variables from dotenv
load_dotenv()

# Access the API key from environment variables
api_key = os.getenv("WEATHER_API_KEY")
location = input("Please input your location:")
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"

try:
    # make the API request
    response = requests.get(url)
    response.raise_for_status() # raise an error for bad HTTP response.

    # Parse the json response
    weather_data = response.json()

    # Extract and print key data
    print(f"Weather Information:")
    print(f"Location: {weather_data['location']['name']}, {weather_data['location']['country']}")
    print(f"Temperature (Celsius): {weather_data['current']['temp_c']}°C")
    print(f"Condition: {weather_data['current']['condition']['text']}")
    print(f"Humidity: {weather_data['current']['humidity']}%")
    print(f"Wind Speed: {weather_data['current']['wind_kph']} kph")
except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")

