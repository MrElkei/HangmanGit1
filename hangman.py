# Veicam mūsu izveidotās klases Game ielādi
# Pārliecinies, ka mapē gameplay ir izveidots tukšs vails ar nosaukumu __init__.py
from gameplay.game import Game
from scripts.display import Display
from animations.animationHangman import AnimationHangman
from animations.animationWelcome import AnimationWelcome
import random
import os
import time
import sys
#TODO ieviest cheatcodes
#TODO exit
#TODO Animēta atvadīšanās
#TODO Uzlabot vārdu atlases parametrus - sekojošu līdzskaņu un patskaņu skaits? dalījums zilbēs?
#TODO Krāsu izvade?
#TODO pārliecināties, ka saraksts nesatur vienādus vārdus
#TODO Highscore
#TODO Tezaurus skaidrojums

display = Display()
display.updateLine(2, 1, "Grūtības pakāpes:")
display.updateLine(2, 2, "    1. viegla")
display.updateLine(2, 3, "    2. vidēja")
display.updateLine(2, 4, "    3. grūta")
for n in range(0, 3):
    display.animate(left_colums_animation=AnimationHangman())

display.animate(middle_column_animation=AnimationWelcome())

display.updateLine(1, 7, "Laipni lūdzam karātavās! Izvēlies grūtības pakāpi 1, 2 vai 3")
display.refresh()
deriga_ievade = False
grutibas_pakape_file = ""
grutibas_pakape = ""
while not deriga_ievade:
    try:
        ievade = input("\nGrūtības pakāpe: ")
    except EOFError:
        display.updateLine(1, 7, "Saņemta \"EOFError\" kļūda!")
        display.refresh()
        time.sleep(3)
    except KeyboardInterrupt:
        display.updateLine(1, 7, "Paldies par spēli gaidīsim tevi atkal!")
        display.refresh()
        sys.exit()
    else:
        if ievade == '1':
            grutibas_pakape_file = 'easy_words.txt'
            deriga_ievade = True
            grutibas_pakape = "viegla"
        elif ievade == '2':
            grutibas_pakape_file = 'medium_words.txt'
            deriga_ievade = True
            grutibas_pakape = "vidēja"
        elif ievade == '3':
            grutibas_pakape_file = 'hard_words.txt'
            deriga_ievade = True
            grutibas_pakape = "grūta"
        else:
            display.updateLine(1, 7, "Nepareizi izvēlēta grūtības pakāpe! Izvēlies 1, 2 vai 3")
            display.refresh()

# Izveido absolūtu ceļu līdz words.txt failam
# 1. Atrod skripta atrašanās vietu
script_dir = os.path.dirname(os.path.realpath(__file__))
# 2. Pievieno words.txt atrašanās vietu
words_file = os.path.join(script_dir, 'data', grutibas_pakape_file)

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
            except EOFError:
                print('\nSaņemta "EOFError" kļūda!')
                time.sleep(3)
            except KeyboardInterrupt:
                print('\nPaldies par spēli gaidīsim tevi atkal!')
                sys.exit()
            else:
                if atbilde not in ["JĀ", "JA", "J"]:
                    vai_turpināt = False
            