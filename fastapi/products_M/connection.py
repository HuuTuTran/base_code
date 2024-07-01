from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://sa:1234567@127.0.0.1:3306/mini_data?charset=utf8mb4&collation=utf8mb4_general_ci"
# Define database connection engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()