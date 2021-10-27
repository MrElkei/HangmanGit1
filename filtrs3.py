# Veicam mūsu izveidotās klases Game ielādi
# Pārliecinies, ka mapē gameplay ir izveidots tukšs vails ar nosaukumu __init__.py
from gameplay.game import Game
import random
import os

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
words_list = words_str.splitlines()

# print(words_list)

word_len = []
for word in words_list:
    word_len.append(len(word))

word_len_unique = []
for word in words_list:
    word_len_unique.append(len(set(word)))

popular_letters = ['A', 'S', 'I', 'E', 'T', 'R', 'N', 'P', 'Ā']
popular_letters_count = []
for word in words_list:
    count = 0
    for letter in set(word):
        if letter.upper() in popular_letters:
            count += 1
    popular_letters_count.append(count)

unpopular_letters = ['G', 'Ņ', 'Ļ', 'Ģ', 'Ķ', 'Ž', 'H', 'Č']
unpopular_letters_count = []
for word in words_list:
    count = 0
    for letter in set(word):
        if letter.upper() in unpopular_letters:
            count += 1
    unpopular_letters_count.append(count)

score_list = []
for n in range(738, 739):

    #Vārda garuma punktu sadale
    word_len_score = 0
    if word_len[n] < 7:
        pass
    elif word_len[n] < 10:
        word_len_score += 1
    elif word_len[n] < 14:
        word_len_score += 2
    else:
        word_len_score += 3


    #Unikālo burtu punktu sadale
    letter_repetitiveness_score = 0
    if word_len[n] > 7:
        letter_repetitiveness = int(((word_len[n] - word_len_unique[n]) * 100) / word_len[n])
        if letter_repetitiveness < 40:
            letter_repetitiveness_score +=3
        elif letter_repetitiveness < 60:
            letter_repetitiveness_score += 2
        elif letter_repetitiveness < 80:
            letter_repetitiveness_score += 1
        else:
            pass

    #Nepopulāro burtu punktu sadale

    unpopular_letter_repetitiveness = int((unpopular_letters_count[n] * 100) / word_len[n])

    #print(f'unpopular_letter_repetitiveness: {unpopular_letter_repetitiveness}')

    unpopular_letter_score = 0
    if unpopular_letter_repetitiveness < 10:
        pass
    elif unpopular_letter_repetitiveness < 30:
        unpopular_letter_score += 1
    elif unpopular_letter_repetitiveness < 40:
        unpopular_letter_score += 2
    else:
        unpopular_letter_score +=3


    #Populāro burtu punktu sadale
    popular_letter_repetitiveness = int((popular_letters_count[n] * 100) / word_len[n])

    #print(f'popular_letter_repetitiveness: {popular_letter_repetitiveness}')

    popular_letter_score = 0
    if popular_letter_repetitiveness < 20:
        popular_letter_score +=3
    elif popular_letter_repetitiveness < 30:
        popular_letter_score += 2
    elif popular_letter_repetitiveness < 50:
        popular_letter_score += 1
    else:
        pass

    #abc = list('AĀBCČDEĒFGĢHIĪJKĶLĻMNŅOPRSŠTUŪVZŽ')
    #for l in abc:
    #    print(f"{l} = {words_str.count(l)}")

    print(words_list[n])
    print(f'Vārda garums: {word_len[n]}, score: {word_len_score}')
    print(f'Unikālo butu skaits: {word_len_unique[n]}, score: {letter_repetitiveness_score}')
    print(f'Populāro burtu skaits: {popular_letters_count[n]}, score: {popular_letter_score}')
    print(f'Nepopulāro burtu skaits: {unpopular_letters_count[n]}, score: {unpopular_letter_score}')

    score = word_len_score + letter_repetitiveness_score + popular_letter_score + unpopular_letter_score
    #print(f'Score: {score}')
    score_list.append(score)

print('Score novērtējumu sadalījums:')
for i in range(1, 12):
    print(f"{i}: {score_list.count(i)}")