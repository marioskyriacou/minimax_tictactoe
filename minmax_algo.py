from multiplayer import *
import math
def minmax_algo(board, maximizer, depth, max_depth):
    '''
    MiniMax Algorithm:
    Check if the X win and return -1 since the AI player lose else return 1 since the AI player wins if is a draw return 0.
    This function is responsible to find the optimal path and return the evaluation score (-1,0,1)
    :input1: board: (list) - a current situation of the game
    :input2: maximizer: (bool) - if its maximizers turn
    :input3&4: depth, max_depth: (int) - the depth of the game
    '''
    # check if the 'X' player wins the game
    if check_winner(board, 'X'):
        return -1
    # check if the 'O' player wins the game
    elif check_winner(board, 'O'):
        return 1
    # check if is a draw
    elif (not check_winner(board, 'O') and table_count(board)) or depth == max_depth:
        return 0
    elif (not check_winner(board, 'X') and table_count(board)) or depth == max_depth:
        return 0

    # if maximizing, set the maximum evaluation to -inf
    if maximizer:
        max_eval = -math.inf
        # check all the available positions
        for pos in range(len(board)):
            if available_position(board, pos):
                board = add_marker(board, 'O', pos)
                # the add one more value to depth and the next player simulation move
                max_eval = max(max_eval, minmax_algo(board, not maximizer, depth+1, max_depth))
                board = add_marker(board, '-', pos)
        return max_eval
    else:
        # if not maximizing, set the maximum evaluation to inf
        min_eval = math.inf
        # check all the available positions
        for position in range(len(board)):
            if available_position(board, position):
                board = add_marker(board, 'X', position)
                # the add one more value to depth and the next player simulation move
                min_eval = min(min_eval, minmax_algo(board, not maximizer, depth+1, max_depth))
                board = add_marker(board, '-', position)
        return min_eval


def best_move(board, max_depth):
    '''
    This function determines the optimal move for the AI player using Mini Max algorithm return the optimal position
    :input1: board: (list) - a current situation of the game
    :param max_depth:
    :input3&4: max_depth: (int) - the depth of the game
    '''

    best_eval = -math.inf
    # empty position
    bestMove = None
    # For all the available position use minimax algorithm return the optimal move position
    for position in range(len(board)):
        if available_position(board, position):
            board = add_marker(board,'O', position)
            evaluation = minmax_algo(board, False, 0, max_depth)
            board = add_marker(board,'-', position) # undo the move
            # f the evaluation score is better than the best score the position is the optimal
            if evaluation > best_eval:
                best_eval = evaluation
                bestMove = position

    return bestMove



def minmax_main():
        table = ['-' for i in range(9)]
        player, comp = 'X', 'O'
        player_turn = True
        turn = 1

        while True:
            display_board(table)
            if player_turn:
                table = player_move(table=table, letter=player)
                print(f'Player ({player}) Move: Turn: {turn}')
            else:
                comp_move = best_move(board=table, max_depth=7)
                table[comp_move] = comp
                print(f'Computer ({comp}) Move:Turn {turn}')

            if check_winner(table, player):
                display_board(table)
                print('X Wins!!')
                break
            elif check_winner(table, comp):
                display_board(table)
                print('Computer Wins!')
                break
            elif not check_winner(table, comp) and table_count(table):
                print('Tie')
            elif not check_winner(table, player) and table_count(table):
                print('Tie')
                break

            player_turn = not player_turn
            turn = turn + 1











