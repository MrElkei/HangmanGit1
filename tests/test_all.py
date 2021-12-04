import pytest
from gameplay.game import Game


def test_game_vards():
    vards = "test"
    game = Game(vards, "viegla")
    assert game.vards == vards.upper()


        
