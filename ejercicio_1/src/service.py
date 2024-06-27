from sqlalchemy.orm import Session
from fastapi import status
from datetime import datetime
from src.models import Cars, Subsidiary
from src.tools.insert_cars_script import insert_cars_seed
from src.schemas import CarCreate
from src.exceptions import validate_existe_subsidiary_id


class CarsService():
    def __init__(
            self,
            db              :   Session
            ):
        self.__db   = db


    async def get_cars(self, brand: str, subsidiaryName: str):
        try:
            cars_count = self.__db.query(Cars)
            if cars_count.count() <= 0:
                await insert_cars_seed(db=self.__db)

            subsidiary_query = self.__db.query(Subsidiary).filter(Subsidiary.name == subsidiaryName).first()
            
            if subsidiary_query:

                cars_query = self.__db.query(Cars).filter(Cars.brand.ilike(f'%{brand}%'), Cars.subsidiary_id == subsidiary_query.subsidiary_id).all()

                return {
                        "status_code"         :   status.HTTP_200_OK,
                        "total_docs"          :   len(cars_query),
                        "message"             :   "Car list",
                        "payload"             :   cars_query
                }
        
            cars_query = self.__db.query(Cars).filter(Cars.brand.ilike(f'%{brand}%')).all()

            return {
                    "status_code"         :   status.HTTP_200_OK,
                    "total_docs"          :   len(cars_query),
                    "message"             :   "Car list",
                    "payload"             :   cars_query
            }
        
        except Exception as e:
            raise e


    def set_car(self, car: CarCreate):
        try:
            # VALIDA QUE EXISTA EL ID ENVIADO EN EL BODY
            subsidiary_query = self.__db.query(Subsidiary).filter(Subsidiary.subsidiary_id == car.subsidiary_id).first()
            validate_existe_subsidiary_id(subsidiary=subsidiary_query)
            
            create_new_cart = Cars(
                year                                =   car.year,
                model                               =   car.model.lower(),
                brand                               =   car.brand.lower(),
                subsidiary_id                       =   car.subsidiary_id,
                created_at                          =   datetime.now()
            )

            self.__db.add(create_new_cart)
            self.__db.commit()
            self.__db.refresh(create_new_cart)

            return {
                "status_code": status.HTTP_201_CREATED,
                "message": "Car created",
                "payload": create_new_cart
            }

        except Exception as e:
            raise e