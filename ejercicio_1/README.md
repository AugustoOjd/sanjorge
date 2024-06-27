# Api Cars

Api para lista autos con sus respectivas marcas y crear nuevos

## Architecture/Structure


```
.ejercicio_1
├── src/
|
├── ├── tools
|   └── insert_cars_script
|
│   ├── db_connection.py      
│   ├── models.py      
│   ├── dependencies.py   
│   ├── exceptions.py     
│   ├── routers.py         
│   ├── schemas.py         
│   ├── services.py        
│   └── main.py
|
├── requirements   
├── .env.schema
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── main.py
└── README.md
```


## Stack

- Fastapi
- Python
- Pydantic
- sqlachemy


## Endpoints 

[GET] http://localhost:8090/api/cars?brand=chevrolet&subsidiaryName=sanluis

[POST] http://localhost:8090/api/cars

## Run api docker

- add .env
- docker compose up --build
- [localhost](http://localhost:8090/docs)


## Testing api local

- pip install -r requirements.txt
- uvicorn main:app --reload
- http://localhost:8000/docs














