import pytest
from gameplay.game import Game
from scripts.EnglishApi import EnglishWords


def test_game_vards():
    vards = "test"
    game = Game(vards, "viegla")
    assert game.vards == vards.upper()


def test_game_aizklata_varda_generators():
    vards = "a"*5
    game = Game(vards, "viegla")
    assert len(game._aizklata_varda_generators()) == 5


def test_english_word_request():
    english = EnglishWords()
    words = english.get_words()
    assert type(words) == list
    assert len(words) == 200