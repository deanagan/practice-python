def determine_winner(game_result):

    # check horizontals
    b = list(filter(lambda a: all([a == a[0]*3, a != '...']), game_result))
    if len(b) == 1:
        return b[0][0]

    # check verticals
    b = list(filter(lambda a: all(
        [''.join(a) == a[0]*3, ''.join(a) != '...']), zip(*game_result)))
    if len(b) == 1:
        return b[0][0]

    # check diagonals
    if all(game_result[0][0] == game_result[i][i] for i in range(0, 3)) and game_result[0][0] != '.':
        return game_result[0][0]

    if all(game_result[0][2] == game_result[i][j] for i, j in zip(range(0, 3), range(2, -1, -1))) and game_result[0][2] != '.':
        return game_result[0][2]

    return 'D'
