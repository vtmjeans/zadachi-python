class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError()
    
    player1, player1move = players[0]
    player2, player2move = players[1]
    valid_moves = ['R', 'P', 'S']

    if player1move not in valid_moves:
        raise NoSuchStrategyError()
    if player2move not in valid_moves:
         raise NoSuchStrategyError()
    win_combo = {
        'R': 'S',
        'S': 'P',
        'P': 'R'
    }

    if player1move == player2move:
        return f"{player1} {player1move}"

    if win_combo[player1move] == player2move:
        return f"{player1} {player1move}"
    else:
        return f"{player2} {player2move}"
def mistake_retrn(players):
    try:
        return rps_game_winner(players)
    except WrongNumberOfPlayersError:
        return "WrongNumberOfPlayersError"
    except NoSuchStrategyError:
        return "NoSuchStrategyError"
    
print(rps_game_winner([["Maksonchik", "P"], ["Vanya", "R"]]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))
print(mistake_retrn([["P1", "R"], ["P2", "S"], ["P3", "P"]]))



    