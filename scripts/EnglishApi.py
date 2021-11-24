import os
import requests
import json

Class EnglishWords:
    def __init__(self, wordE):
        self.wordE = wordE
        self.

URL='https://random-word-api.herokuapp.com/word?number=1'def get_words(num):
    response=requests.get(URL+str(num)).text
    return json.loads(response)



    english_words_file = os.path.join(script_dir, '..', 'data', 'english_words.txt')

    with open(easy_words_file, 'w', encoding='utf-8') as file:
	file.write(easy_words)