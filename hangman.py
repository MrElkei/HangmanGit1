# Veicam mūsu izveidotās klases Game ielādi
# Pārliecinies, ka mapē gameplay ir izveidots tukšs vails ar nosaukumu __init__.py
from gameplay.game import Game
from helpers.clear import clearConsole
import random
import os

# TODO uzlabot izvades lasāmību.

# Izveido absolūtu ceļu līdz words.txt failam
# 1. Atrod skripta atrašanās vietu
script_dir = os.path.dirname(os.path.realpath(__file__))
# 2. Pievieno words.txt atrašanās vietu
words_file = os.path.join(script_dir, 'data', 'words.txt')

# Lasām vārdu sarakstu, kā tekstu
with open(words_file, 'r', encoding='utf-8') as file:
	words_str = file.read()

# Pārveidojam vārdu sarakstu no teksta formāta uz List formātu
# TODO pārliecināties, ka saraksts nesatur vienādus vārdus
words_list = words_str.split('\n') # use .splitline() for universal code

# Sajauc vārdu secību
random.shuffle(words_list)

# Izveido karodziņu spēles turpinājumam
vai_turpināt = True

# Uzsāk spēles pamatciklu
while words_list and vai_turpināt:
    clearConsole()
    
    # Izveidojam jaunu spēles instanci un nododam tai mināmo vārdu
    game = Game(words_list.pop())

    # Palaižam spēli
    game.play()

    # Pārliecināties vai turpināt spēli
    atbilde = input("Vai turpināt spēli (jā / nē): ").upper()
    if not (atbilde == "JĀ" or atbilde == "JA" or atbilde == "J"):
        vai_turpināt = False

    #if atbilde not in ["JĀ", "JA", "J"]:
    #    pass