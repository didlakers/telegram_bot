import requests
from typing import List, Dict
from config import  API_KEY



# def api_request(endpoint: str, params={}) -> requests.Response:
#     params['key'] = API_KEY
#     return requests.get(f'{API_BASE_URL}/')

def movie_search(film_name: str):
    response = requests.get('https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10query=', headers={
        'accept': "application/json",
        'X-API-KEY': API_KEY,
        'query' : film_name
    })
    print(response.text)
    return response

movie_search('Jane Air')

