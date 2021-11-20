# Jauns fails
import os

# Izveido absolūtu ceļu līdz words.txt failam
# 1. Atrod skripta atrašanās vietu
"""Finds the exact location of the game in your computer"""
script_dir = os.path.dirname(os.path.realpath(__file__))
# 2. Pievieno words.txt atrašanās vietu
"""Adding words.txt file, which contains all the guessable words, location"""
words_file = os.path.join(script_dir, '..', 'data', 'words.txt')

# Lasām vārdu sarakstu, kā tekstu
"""Reading words list as text"""
with open(words_file, 'r', encoding='utf-8') as file:
	words_str = file.read()

# Pārveidojam vārdu sarakstu no teksta formāta uz List formātu
# TODO pārliecināties, ka saraksts nesatur vienādus vārdus
words_list = words_str.splitlines()

# print(words_list)
"""1st difficulty setting calculates word length - the longer the word, the higher the difficulty"""
word_len = []
for word in words_list:
    word_len.append(len(word))

word_len_unique = []
for word in words_list:
    word_len_unique.append(len(set(word)))

"""2nd difficulty setting calculates the amount of most popular letters for guessing in the word.
The higher the amount of these letters, the easier the difficulty"""
popular_letters = ['A', 'S', 'I', 'E', 'T', 'R', 'N', 'P', 'Ā']
popular_letters_count = []
for word in words_list:
    count = 0
    for letter in set(word):
        if letter.upper() in popular_letters:
            count += 1
    popular_letters_count.append(count)

"""2nd difficulty setting calculates the amount of least popular letters for guessing in the word.
The higher the amount of these letters, the harder the difficulty"""
unpopular_letters = ['G', 'Ņ', 'Ļ', 'Ģ', 'Ķ', 'Ž', 'H', 'Č']
unpopular_letters_count = []
for word in words_list:
    count = 0
    for letter in set(word):
        if letter.upper() in unpopular_letters:
            count += 1
    unpopular_letters_count.append(count)

score_list = []
for n in range(0, len(words_list)):

"""Score count for word length - for more letters is added higher score, which gives additional points to overall difficulty"""
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
    """Unique letter count function. The more the reppetitive letters are in the word, the easier the overall difficulty"""
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
    """Unpopular letter for guessing point count"""

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
    """Score for popular letter count."""
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

    score = word_len_score + letter_repetitiveness_score + popular_letter_score + unpopular_letter_score
    score_list.append(score)

print('Score novērtējumu sadalījums:')
for i in range(1, 12):
    print(f"{i}: {score_list.count(i)}")

"""Function for word list split in 3 difficulties - easy, medium and hard. Also added a chance for user to choose the difficulty of the game"""
easy_words_list = []
medium_words_list = []
hard_words_list = []
for index, word in enumerate(words_list):
    if score_list[index] < 5:
        easy_words_list.append(word)
    elif score_list[index] < 7:
        medium_words_list.append(word)
    else:
        hard_words_list.append(word)

easy_words = '\n'.join(easy_words_list)
medium_words = '\n'.join(medium_words_list)
hard_words = '\n'.join(hard_words_list)

easy_words_file = os.path.join(script_dir, '..', 'data', 'easy_words.txt')
medium_words_file = os.path.join(script_dir, '..', 'data', 'medium_words.txt')
hard_words_file = os.path.join(script_dir, '..', 'data', 'hard_words.txt')

"""3 different files for difficulties added, which include only words of the needed difficulties in the files with acording name"""
with open(easy_words_file, 'w', encoding='utf-8') as file:
	file.write(easy_words)

with open(medium_words_file, 'w', encoding='utf-8') as file:
	file.write(medium_words)

with open(hard_words_file, 'w', encoding='utf-8') as file:
	file.write(hard_words)

