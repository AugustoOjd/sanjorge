import json
import requests
from app import app

@app.task
def fetch_and_write_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        
        with open('weather_data.json', 'w') as f:
            json.dump(weather_data, f, indent=4)
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")


def req_main(req: int):
    for _ in range(req):
        fetch_and_write_weather_data.delay()