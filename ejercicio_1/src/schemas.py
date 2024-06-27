from pydantic import BaseModel, field_validator, Field
from datetime import datetime


# SCHEMAS BASE Y DE RESPONSE
class SubsidiaryBase(BaseModel):
    subsidiary_id       :   int             = Field(None, alias='id')
    name                :   str             = Field(None, alias='name')
    created_at          :   datetime | str  = Field(None, alias='createdAt')

    class Config:
        populate_by_name = True


class CarBase(BaseModel):
    car_id              :   int             = Field(None, alias='id')
    year                :   int             = Field(None, alias='year')
    model               :   str             = Field(None, alias='model')
    brand               :   str             = Field(None, alias='brand')
    created_at          :   datetime | str  = Field(None, alias='createdAt')

    subsidiary          :   SubsidiaryBase

    class Config:
        from_attributes = True
        populate_by_name = True


class CarResponse(BaseModel):
    status_code         :   str | int
    total_docs          :   int
    message             :   str
    payload             :   list[CarBase] = []




# SCHEMAS PARA CREACION
class CarCreate(BaseModel):
    year                :   int
    @field_validator('year')
    def check_year(cls, value):
        if not value:
            raise ValueError('The brand cannot be empty')
        current_year = datetime.now().year
        if not (1886 <= value <= current_year):
            raise ValueError(f'The year must be between 1886 and {current_year}')
        return value
    
    brand               :   str
    @field_validator('brand')
    def check_brand(cls, value):
        if not value:
            raise ValueError('The brand cannot be empty')
        if len(value) < 2:
            raise ValueError('The brand must be at least 2 characters')
        return value
    
    model               :   str
    @field_validator('model')
    def check_model(cls, value):
        if not value:
            raise ValueError('The model cannot be empty')
        if len(value) < 2:
            raise ValueError('The model must be at least 2 characters')
        return value
    
    subsidiary_id       :   int
    @field_validator('subsidiary_id')
    def check_subsidiary_id(cls, value):
        if not value:
            raise ValueError('The subsidiary_id cannot be empty')
        if value <= 0:
            raise ValueError('The subsidiary id cannot be 0 or negative')
        return value


class CarCreateResponse(BaseModel):
    status_code         :   str | int
    message             :   str
    payload             :   CarBase | None = None