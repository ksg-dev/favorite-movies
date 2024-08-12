# Responsible for communicating with Movie API
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.environ["MOVIE_API_KEY"]
TOKEN = os.environ["MOVIE_API_READ_TOKEN"]
GET_URL = "https://api.themoviedb.org/3/search/movie"
DETAILS_URL = "https://api.themoviedb.org/3/movie"


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

        movie_list = []

        for movie in movie_data:
            movie_list.append(movie)

        return movie_list


def get_details(movie_api_id):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    query_str = f"{DETAILS_URL}/{movie_api_id}"

    response = requests.get(query_str, headers=headers)
    response.raise_for_status()
    data = response.json()
    title = data['title']
    img_url = data['poster_path']
    year = data['release_date'].split('-')[0]
    description = data['overview']

    movie_details = {
        "title": title,
        "img_url": img_url,
        "year": year,
        "description": description
    }

    return movie_details




