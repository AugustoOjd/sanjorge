from src.models import Cars, Subsidiary
from sqlalchemy.orm import Session
from datetime import datetime
import random

subsidiaries_list = [
    {
        "name": "Uspallata"
    },
    {
        "name": "San Juan"
    },
    {
        "name": "Mendoza"
    },
    {
        "name": "San Rafael"
    },
    {
        "name": "San Luis"
    },
    {
        "name": "La Rioja"
    },
    {
        "name": "Catamarca"
    },
    {
        "name": "Tucumán"
    },
    {
        "name": "Salta"
    },
    {
        "name": "Jujuy"
    }
]


cars_list = [
    {
        "year": 2020,
        "model": "Onix",
        "brand": "Chevrolet"
    },
    {
        "year": 2021,
        "model": "Cruze",
        "brand": "Chevrolet"
    },
    {
        "year": 2019,
        "model": "Tracker",
        "brand": "Chevrolet"
    },
    {
        "year": 2018,
        "model": "S10",
        "brand": "Chevrolet"
    },
    {
        "year": 2022,
        "model": "Equinox",
        "brand": "Chevrolet"
    },
    {
        "year": 2017,
        "model": "Spark",
        "brand": "Chevrolet"
    },
    {
        "year": 2020,
        "model": "Camaro",
        "brand": "Chevrolet"
    },
    {
        "year": 2021,
        "model": "Blazer",
        "brand": "Chevrolet"
    },
    {
        "year": 2018,
        "model": "Captiva",
        "brand": "Chevrolet"
    },
    {
        "year": 2019,
        "model": "Colorado",
        "brand": "Chevrolet"
    },
        {
        "year": 2020,
        "model": "Corolla",
        "brand": "Toyota"
    },
    {
        "year": 2021,
        "model": "Civic",
        "brand": "Honda"
    },
    {
        "year": 2019,
        "model": "Model 3",
        "brand": "Tesla"
    },
    {
        "year": 2018,
        "model": "Mustang",
        "brand": "Ford"
    },
    {
        "year": 2022,
        "model": "CX-5",
        "brand": "Mazda"
    },
    {
        "year": 2017,
        "model": "Impreza",
        "brand": "Subaru"
    },
    {
        "year": 2020,
        "model": "A4",
        "brand": "Audi"
    },
    {
        "year": 2021,
        "model": "C-Class",
        "brand": "Mercedes-Benz"
    },
    {
        "year": 2018,
        "model": "3Series",
        "brand": "BMW"
    },
    {
        "year": 2019,
        "model": "Altima",
        "brand": "Nissan"
    }
]


async def insert_subsidiaries(db: Session):
    try:
        for subsidiary in subsidiaries_list:
            if subsidiary:
                new_subsidiary = Subsidiary(
                    name       = subsidiary.get('name').lower(),
                    created_at = datetime.now()
                )

            db.add(new_subsidiary)
        
        db.commit()
    except Exception as e:
        print('error inser subsidiaries')
        db.rollback()
        raise e



async def insert_cars_seed(db: Session):
    try:
        await insert_subsidiaries(db=db)

        subsidiaries_query = db.query(Subsidiary).all()

        subsidiaries_id_list = []

        for s in subsidiaries_query:
            subsidiaries_id_list.append(s.subsidiary_id)

        for car in cars_list:
            if car:
                new_car = Cars(
                    year                                = car.get('year'),
                    model                               = car.get('model').lower(),
                    brand                               = car.get('brand').lower(),
                    subsidiary_id                       = random.choice(subsidiaries_id_list),
                    created_at                          = datetime.now()
                )

            db.add(new_car)
        
        db.commit()
    except Exception as e:
        print('error inser cars')
        db.rollback()
        raise e