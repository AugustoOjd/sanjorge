from app.celery import app
import random
import requests
import json


# @app.task(max_retries=3, retry_backoff=5)
# def write_numbers(self, count, **kwargs):
#     with open('random_number.txt', 'w') as file:
#         for _ in range(count):
#             random_number = random.randint(1, 50)
#             file.write(f'{random_number}\n')


# @app.task(max_retries=3, retry_backoff=5)
# def write_text(count, **kwargs):
#     letras = ["s", 'd', 'g', 'b', 'j', 'x']
#     with open('random_text.txt', 'w') as file:
#         for _ in range(count):
#             random_letra = random.choice(letras)
#             file.write(f'{random_letra}\n')

@app.task(bind=True, name='weather-api', max_retries=3, retry_backoff=True, default_retry_delay=30)
def write_response(self, count):
    try:
        responses = []
        for _ in range(count):
            req_api = requests.get(
                'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
            )
            
            if req_api.status_code == 200:
                data = req_api.json()
                # print(req_api.json()['latitude'])
                zone = {
                        "latitude": data['latitude'],
                        "longitude": data['longitude'],
                        "generationtime_ms": data['generationtime_ms'],
                        "utc_offset_seconds": data['utc_offset_seconds'],
                        "timezone": data['timezone'],
                        "timezone_abbreviation": data['timezone_abbreviation'],
                        "elevation": data['elevation'],
                        "current": {
                            "time": data['current']['time'],
                            "interval": data['current']['interval'],
                            "temperature_2m": data['current']['temperature_2m'],
                            "wind_speed_10m": data['current']['wind_speed_10m']
                        }
                }

                responses.append(zone)
            else:
                raise Exception(f"API request failed with status code {req_api.status_code}")

        with open('weather_response.json', 'w') as file:
            json.dump(responses, file, indent=2)
        
        task_name = self.name
        task_id = self.request.id
        
        return f"Task completed successfully! Task name: {task_name}, Task ID: {task_id}"

    except Exception as e:
        raise self.retry(exc=e, countdown=10)


