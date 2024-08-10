# Responsible for communicating with Movie API
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.environ["MOVIE_API_KEY"]
TOKEN = os.environ["MOVIE_API_READ_TOKEN"]
GET_URL = "https://api.themoviedb.org/3/search/movie"


class GetMovie:
    def __init__(self, title):
        self.title = title
        self.key = API_KEY
        self.token = TOKEN
        self.movie_details = self.find_movie(title)


    def find_movie(self, title):
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TOKEN}"
        }

        parameters = {
            "query": title
        }

        response = requests.get(GET_URL, headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()
        movie_data = data["results"]
        print(movie_data)



movie = GetMovie("Matrix")
print(movie)

