#3e27e015895e9b5c1c662edef0a97466
import requests
import json
import datetime
import os

# Fetch API key and city from environment variables
API_KEY = os.getenv("API_KEY", "3e27e015895e9b5c1c662edef0a97466")  # Replace 'your_api_key' for testing purposes if needed
CITY = os.getenv("CITY", "London")

def fetch_weather_data():
    # Correct OpenWeatherMap API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    
    try:
        # Make a GET request to the OpenWeatherMap API
        response = requests.get(url)
        # Check if the request was successful
        response.raise_for_status()
        # Parse the JSON data from the response
        data = response.json()
        
        # Print the fetched weather data
        print("Fetched weather data:", json.dumps(data, indent=2))

        # Optionally save data to a file
        with open("weather_data.json", "w") as f:
            json.dump(data, f)
        print("Weather data saved successfully.")

    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    print("Data ingestion started at:", datetime.datetime.now())
    fetch_weather_data()
    print("Data ingestion completed at:", datetime.datetime.now())
    print("\n\n")
