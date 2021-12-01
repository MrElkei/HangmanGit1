# Hangman
## Table of the content
- [About the project](https://github.com/artishox/hangman#about-the-project)
- [Authors](https://github.com/artishox/hangman#authors)
- [Printscreen](https://github.com/artishox/hangman#printscreen)
- [Key features](https://github.com/artishox/hangman#key-features)
- [Dependencies](https://github.com/artishox/hangman#dependencies)


## About the project
The variant of the popular word guessing game "Hangman". The game was developed as an independent project for the FITA Python classes. The project consists of several distinct parts - a script that splits a list of words into difficulties and the game that allows playing through a large number of words in Latvian and English. The interface of the game is in Latvian. At the beginning of the game, a player can choose a difficulty level. The game loops through a wast selection of words both in Latvian and English. The game has a unique interface that provides both multi-column output and ASCII animations for the console output.

## Authors
[Artis Kinens](https://github.com/artishox), [Gunta Sončika](https://github.com/Warkrool), [Andris Vovers](https://github.com/vovers711), [Lauris Kauķis](https://github.com/MrElkei) and Daiga Zentele.

## Printscreen
```
        |                                _____                                          |
  +---+ |             __ __ ___    ____ /____/_________ _    _____   _____ __           | Grūtības pakāpes:
  |   | |            / //_//   |  / __ \/   |/_  __/   | |  / /   | / ___// /           |     1. viegla
  O   | |           / ,<  / /| | / /_/ / /| | / / / /| | | / / /| | \__ \/ /            |     2. vidēja
 /|\  | |          / /| |/ ___ |/ _, _/ ___ |/ / / ___ | |/ / ___ |___/ /_/             |     3. grūta
 / \  | |         /_/ |_/_/  |_/_/ |_/_/  |_/_/ /_/  |_|___/_/  |_/____(_)              |     4. English Word
      | |                                                                               |
======= | Laipni lūdzam karātavās! Izvēlies grūtības pakāpi 1, 2, 3 vai 4               |

Grūtības pakāpe:

======================================================================================================================

        |    --== Laipni lūgti karātāvās! ==--                                          | Statistika:
  +---+ |                                                                               |    Dzīvības: 2
  |   | | Diemžēl tu neuzminēji, mēģini vēlreiz!                                        |    Vārda  garums: 8
  O   | | Minamajā vārdā nav burta "U"                                                  |    Minēto burtu sk.: 7
 /|\  | |                                                                               |    Minēto vārdu sk.: 0
      | |                                                                               |
      | | Tavs progress: ----E-IS                                                       | Grūtības pakāpe: viegla.
======= |                                                                               | Raksti EXIT, lai izietu.

Ieraksti burtu vai vārdu:

======================================================================================================================

        |         __  ________    _____    ____  ___    __                              | Statistika:
  +---+ |        / / / /__  / |  / /   |  / __ \/   |  / /                              |    Dzīvības: 3
  |   | |       / / / /  / /| | / / /| | / /_/ / /| | / /                               |    Vārda  garums: 6
  O   | |      / /_/ /  / /_| |/ / ___ |/ _, _/ ___ |/_/                                |    Minēto burtu sk.: 9
 /|   | |      \____/  /____/___/_/  |_/_/ |_/_/  |_(_)                                 |    Minēto vārdu sk.: 0
      | |                                                                               |
      | | Apsveicu tu uzminēji vārdu APKURE. Spēles laks (hh:mm:ss) 0:00:55.793427      | Grūtības pakāpe: viegla.
======= |                                                                               | Raksti EXIT, lai izietu.

Vai turpināt spēli (jā / nē):
```

## Key features
The split_difficulty.py script provides an easy way to sort a list of words into three difficulties that can then be used for the "Hangman" game.
The Display class provides a universal interface to format multi-column output in the console:
```
    +-------------------+----------------------------------------------+--------------------+
    | Column 0, Line 0  | Column 1, Line 0                             | Column 2, Line 0   |
    | Column 0, Line 1  | Column 1, Line 1                             | Column 2, Line 1   |
    | Column 0, Line 2  | Column 1, Line 2                             | Column 2, Line 2   |
    | Column 0, Line 3  | Column 1, Line 3                             | Column 2, Line 3   |
    | Column 0, Line 4  | Column 1, Line 4                             | Column 2, Line 4   |
    +-------------------+----------------------------------------------+--------------------+
```
The class also provides an animation handler to output ASCII animations in the console. The animation frames are stored in the Animation class.

## Dependencies
requests==2.25.0 - used for API requests to obtain English words.

