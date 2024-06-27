from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from src.db_connection import Base
from sqlalchemy.dialects.mysql import INTEGER, BIGINT



class Subsidiary(Base):
    __tablename__                       =   'subsidiary'

    subsidiary_id                       =   Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)
    name                                =   Column(String(255))
    created_at                          =   Column(DateTime)

    subsidiary_owner                    =   relationship('Cars', back_populates='subsidiary')



class Cars(Base):
    __tablename__                       =   'car'

    car_id                              =   Column(Integer, primary_key=True, autoincrement=True, unique=True)
    year                                =   Column(Integer)
    model                               =   Column(String(255), index=True)
    brand                               =   Column(String(255), index=True)
    subsidiary_id                       =   Column(Integer, ForeignKey('subsidiary.subsidiary_id'), index=True)
    created_at                          =   Column(DateTime)

    subsidiary                          =   relationship('Subsidiary', back_populates='subsidiary_owner')







