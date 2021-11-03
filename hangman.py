# Veicam mūsu izveidotās klases Game ielādi
# Pārliecinies, ka mapē gameplay ir izveidots tukšs vails ar nosaukumu __init__.py
from gameplay.game import Game
from scripts.clear import clearConsole
import random
import os

#TODO ieviest cheatcodes
#TODO Universāla ekrāna izvades funkcija
#TODO Karātavu bildīte
#TODO Animācijas ar taimeri
#TODO Uzlabot vārdu atlases parametrus

clearConsole()
print("Sveicināti karātavās!\n")
deriga_ievade = False
grūtibas_pakape = ""
while not deriga_ievade:
    ievade = input("Izvēlies grūtības pakāpi 1, 2 vai 3\n1. Vienkāršie vārdi\n2. Vidēji grūti vārdi\n3. Grūti vārdi\n\nGrūtības pakāpe: ")
    if ievade == '1':
        grūtibas_pakape = 'easy_words.txt'
        deriga_ievade = True
        clearConsole()
        print('Tu izvēlējies vieglo vārdu sarakstu.')
    elif ievade == '2':
        grūtibas_pakape = 'medium_words.txt'
        deriga_ievade = True
        clearConsole()
        print('Tu izvēlējies vidēji grūto vārdu sarakstu.')
    elif ievade == '3':
        grūtibas_pakape = 'hard_words.txt'
        deriga_ievade = True
        clearConsole()
        print('Tu izvēlējies grūto vārdu sarakstu.')
    else:
        clearConsole()
        print("Nepareizi izvēlēta grūtības pakāpe\n")

# Izveido absolūtu ceļu līdz words.txt failam
# 1. Atrod skripta atrašanās vietu
script_dir = os.path.dirname(os.path.realpath(__file__))
# 2. Pievieno words.txt atrašanās vietu
words_file = os.path.join(script_dir, 'data', grūtibas_pakape)

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
    
    # Izveidojam jaunu spēles instanci un nododam tai mināmo vārdu
    game = Game(words_list.pop())

    # Palaižam spēli
    game.play()

    # Pārliecināties vai turpināt spēli
    atbilde = input("Vai turpināt spēli (jā / nē): ").upper()
    clearConsole()
    print('')
    if atbilde not in ["JĀ", "JA", "J"]:
        vai_turpināt = False
        