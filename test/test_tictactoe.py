#Tic-Tac-Toe, sometimes also known as Xs and Os,
#is a game for two players (X and O) who take turns
#marking the spaces in a 3×3 grid. The player who
#succeeds in placing three respective marks in a
#horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

#But we will not be playing this game. You will be the referee for
#this games results. You are given a result of a game and you must
#determine if the game ends in a win or a draw as well as who will
#be the winner. Make sure to return "X" if the X-player wins and "O"
#if the O-player wins. If the game is a draw, return "D".

## Pasting other solutions. These are not my solutions, just pasting for reference:


# def checkio(game_result):
    # all_results = '_'.join(game_result + [''.join(p) for p in zip(*game_result)] + [''.join(game_result[i][i] for i in range(3))] + [''.join(game_result[i][2-i] for i in range(3))])
    # return 'X' if 'XXX' in all_results else 'O' if 'OOO' in all_results else 'D'

import pytest
from src.tictactoe import determine_winner


def test_determine_winner():
    assert determine_winner([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert determine_winner([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert determine_winner([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"

    assert determine_winner([
        "XX.",
        "..X",
        ".OX"]) == "D", "Draw"

    assert determine_winner([
        ".XX",
        "..X",
        ".O."]) == "D", "Draw"

    assert determine_winner([
        "XXX",
        "...",
        ".OX"]) == "X", "Xs wins"
    assert determine_winner([
        ".XX",
        "..X",
        ".OX"]) == "X", "Xs wins"
