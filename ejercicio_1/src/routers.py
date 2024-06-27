from fastapi import APIRouter, Depends
from src.dependencies import validate_api_key
from src.db_connection import SessionLocal
from sqlalchemy.orm import Session
from src.schemas import CarResponse, CarCreate, CarCreateResponse
from src.service import CarsService


cars = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@cars.get(
                    '/',
                    description='Endpoint para listar cars',
                    status_code=200, 
                    dependencies=[Depends(validate_api_key)],
                    tags=['Cars'],
                    response_model=CarResponse
                    )
async def read_cars(brand: str = '', subsidiaryName: str = '', db: Session = Depends(get_db)):
    try:
        car_service = CarsService(db=db)

        return await car_service.get_cars(brand=brand, subsidiaryName=subsidiaryName)
    except Exception as e:
        raise e



@cars.post(
                    '/',
                    description='Endpoint para crear car',
                    status_code=201, 
                    dependencies=[Depends(validate_api_key)],
                    tags=['Cars'],
                    response_model=CarCreateResponse
                    )
async def create_car(car: CarCreate, db: Session = Depends(get_db)):
    try:
        car_service = CarsService(db=db)

        return car_service.set_car(car=car)
    except Exception as e:
        raise e