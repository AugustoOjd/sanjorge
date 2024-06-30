# Celery app

Aplicacion que inserta datos desde la api weather-api (https://open-meteo.com) en un archivo json aplicando tasks por celery

## Context

La intencion es hacer una serie de request simulando un cliente y trabajar esas requests con celery, hacer reintentos con un maximo de 3 en caso de error. 
Al ejecutar el comando de docker compose va crear un archivo json y escribira dentro el

## Architecture/Structure


```
.ejercicio_2
|
├── app/
│   ├── __init__.py  
│   ├── celery.py           # init celery
│   └── tasks.py            # tasks - requests
|
├── requirements   
├── main.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Stack

- Celery
- Docker
- Redis

## Run celery app

- docker-compose up --build

