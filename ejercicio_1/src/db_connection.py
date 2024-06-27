from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()


dbConfig = {
    "dbHost"    : os.environ.get("DB_HOST"),
    "dbUserName": os.environ.get("DB_USER_NAME"),
    "dbPassword": os.environ.get("DB_PASSWORD"),
    "dbName"    : os.environ.get("DB_NAME"),
    "dbport"    : os.environ.get("DB_PORT")
}

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{dbConfig['dbUserName']}:{dbConfig['dbPassword']}@{dbConfig['dbHost']}:{dbConfig['dbport']}/{dbConfig['dbName']}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()