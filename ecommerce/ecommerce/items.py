import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(String, nullable=True)
    url = Column(String, nullable=False)
    image_url = Column(String, nullable=True)


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://munne:munne123@postgres:5432/scraping_db")
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
