from fastapi import FastAPI
from src.db_connection import engine
from fastapi.middleware.cors import CORSMiddleware
from src.routers import cars
from src import db_connection


db_connection.Base.metadata.create_all(bind=engine)


app = FastAPI()


# PARA USAR EN OTRO DOMAIN Y EL FRONT
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)


app.include_router(cars, prefix='/api/cars' )