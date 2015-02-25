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

def checkio(game_result):

   # check horizontals
   b = list(filter(lambda a: all([a == a[0]*3, a != '...']), game_result))
   if len(b) == 1:
       return b[0][0]

   # check verticals
   b = list(filter(lambda a: all([''.join(a) == a[0]*3, ''.join(a) != '...']), zip(*game_result)))
   if len(b) == 1:
       return b[0][0]
           
   # check diagonals
   if all(game_result[0][0] == game_result[i][i] for i in range(0,3)): 
       if game_result[0][0] != '.':
           return game_result[0][0]
          
   if all(game_result[0][2] == game_result[i][j] for i,j in zip(range(0,3), range(2, -1, -1))):
      if game_result[0][2] != '.':
         return game_result[0][2]

   
   return 'D'


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"

    assert checkio([
        "XX.",
        "..X",
        ".OX"]) == "D", "Draw"
    
    assert checkio([
        ".XX",
        "..X",
        ".O."]) == "D", "Draw"

    assert checkio([
        "XXX",
        "...",
        ".OX"]) == "X", "Xs wins"
    assert checkio([
        ".XX",
        "..X",
        ".OX"]) == "X", "Xs wins"
