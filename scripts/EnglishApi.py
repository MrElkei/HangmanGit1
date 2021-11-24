import os
import requests
import json

class EnglishWords:
    def __init__(self):
        self.url = 'https://random-word-api.herokuapp.com/word?number=200'

    def get_words(self):
        response = requests.get(self.url).text
        return json.loads(response)