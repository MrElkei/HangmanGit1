# Veicam mūsu izveidotās klases Game ielādi
# Pārliecinies, ka mapē gameplay ir izveidots tukšs vails ar nosaukumu __init__.py
from gameplay.game import Game
from scripts.clear import clearConsole
import random
import os
import time
#TODO ieviest cheatcodes
#TODO Animēts sveiciens
#TODO Animēta atvadīšanās
#TODO Uzlabot vārdu atlases parametrus - sekojošu līdzskaņu un patskaņu skaits? dalījums zilbēs?
#TODO pārliecināties ka termināls ir pietiekami plats un palielināt to ja nepieciešams
#TODO pārliecināties, ka saraksts nesatur vienādus vārdus

clearConsole()
print("Sveicināti karātavās!\n")
print(" +--+")
print(" O  |")
print("/|\ |")
print("/ \ |")
print("   ===")
time.sleep(1)
deriga_ievade = False
grūtibas_pakape = ""
time.sleep(1)
grutibas_pakape = ""
while not deriga_ievade:
    try:
        ievade = input("Izvēlies grūtības pakāpi 1, 2 vai 3\n\n1. Vienkāršie vārdi\n2. Vidēji grūti vārdi\n3. Grūti vārdi\n\nGrūtības pakāpe: ")
    except:
        print('Saņemta "EOFError" kļūda!')
    else:
        if ievade == '1':
            grūtibas_pakape = 'easy_words.txt'
            deriga_ievade = True
            grutibas_pakape = "viegla"
        elif ievade == '2':
            grūtibas_pakape = 'medium_words.txt'
            deriga_ievade = True
            grutibas_pakape = "vidēja"
        elif ievade == '3':
            grūtibas_pakape = 'hard_words.txt'
            deriga_ievade = True
            grutibas_pakape = "grūta"
        else:
            clearConsole()
            print("Nepareizi izvēlēta grūtības pakāpe\n")

# Izveido absolūtu ceļu līdz words.txt failam
# 1. Atrod skripta atrašanās vietu
script_dir = os.path.dirname(os.path.realpath(__file__))
# 2. Pievieno words.txt atrašanās vietu
words_file = os.path.join(script_dir, 'data', grūtibas_pakape)

# Lasām vārdu sarakstu, kā tekstu
try:
    with open(words_file, 'r', encoding='utf-8') as file:
        words_str = file.read()
except FileNotFoundError:
    print(f'\nDiemžēl neizdevās nolasīt "{words_file}" failu.')
else:
    # Pārveidojam vārdu sarakstu no teksta formāta uz List formātu
    words_list = words_str.splitlines()

    # Sajauc vārdu secību
    random.shuffle(words_list)

    # Izveido karodziņu spēles turpinājumam
    vai_turpināt = True

    # Uzsāk spēles pamatciklu
    while words_list and vai_turpināt:
        
        # Izveidojam jaunu spēles instanci un nododam tai mināmo vārdu
        try:
            game = Game(words_list.pop(), grutibas_pakape)
        except IndexError:
            print(f'\nPaldies par izturību! Visi vārdi šajā grūtības pakāpē ir jau minēti!')
            print(f'Tava izvēlētā gŗutības pakāpe bija: {grutibas_pakape}')
            vai_turpināt = False
        else:
            # Palaižam spēli
            game.play()

            # Pārliecināties vai turpināt spēli
            try:
                atbilde = input("\nVai turpināt spēli (jā / nē): ").upper()
            except:
                print('Saņemta "EOFError" kļūda!')
            else:
                if atbilde not in ["JĀ", "JA", "J"]:
                    vai_turpināt = False
            