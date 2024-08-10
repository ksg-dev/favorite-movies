from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.environ["MOVIE_API_KEY"]
TOKEN = os.environ["MOVIE_API_READ_TOKEN"]
GET_URL = "https://api.themoviedb.org/3/search/movie"


class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["DB_URI"]


class Base(DeclarativeBase):
    pass


