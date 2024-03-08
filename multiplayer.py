import random
'''
The main Rules of the game
https://www.exploratorium.edu/explore/puzzles/tictactoe#:~:text=Rules%20for%20Tic%2DTac%2DToe&text=Players%20take%20turns%20putting%20their,game%20ends%20in%20a%20tie.
------
* The game is played on a 3 × 3 square grid, which is the primary framework of the game. 
* Players place their markings (’O’ or ’X’) on blank squares, with the winner being the first to obtain three of the marks in a row (horizontally, vertically, or diagonally). 
*The game ends when all nine squares are filled, and if no player has three consecutive marks, the game ends in a draw

'''
def display_board(board):
    # game env
    print(f' {board[0]} | {board[1]} | {board[2]} \n '
             f'{board[3]} | {board[4]} | {board[5]} \n '
             f'{board[6]} | {board[7]} | {board[8]}')

def add_marker(table, letter, position):
    # add the letter/marker to the position the player wants
    table[position] = letter
    return table

def available_position(table, position):
    # check if a position is available and return TRUE else return FALSE
    return table[position] == '-'

def player_move(table, letter):
    #The player must enter a number between 0 and 8
    #Check if the player enter a number different than 0 and 8
    #Check if a player enter a letter
    #Check if a player try to enter a taken position from the oponent
    run = True
    while run:
        position = input('Give a a number between 0-8:')
        try:
            position = int(position)
            if available_position(table, position):
                if 0<= position <=8:
                    table = add_marker(table, letter, position)
                    run = False
                    return table
                else:
                    print('Error: Position between 0 and 8!')
            else:
                print('Error: Not available position!')
        except:
            print('Error: Give a number!')

def change_turn(turn, marker):
    # This function is used to change the turn of two player using modulo
    # If a turn is even then return 'X' or 'O' depending on the players turn
    if turn % 2 == 0 and marker == 'X':return 'O'
    elif turn % 2 == 0 and marker == 'O':return 'X'
    elif turn % 2 != 0 and marker == 'X': return 'O'
    elif turn % 2 != 0 and marker == 'O': return 'X'

def check_winner(board, marker):
    # Check if a player win ( all the possible ways for a player to win the game)
    if board[0]==board[1]== board[2]== marker :return True #horizontal
    elif board[3]==board[4]== board[5]== marker:return True
    elif board[6]==board[7]== board[8]== marker:return True
    elif board[0]==board[3]== board[6]== marker:return True #vertical
    elif board[1]==board[4]== board[7]== marker:return True
    elif board[2]==board[5]== board[8]== marker:return True
    elif board[0]==board[4]== board[8]== marker:return True #diagonal
    elif board[6]==board[4]== board[2]== marker:return True
    else:return False

def table_count(table):
    # if positions available are 0 return TRUE else return FALSE
    # this function is also used for the draw
    return table.count('-') == 0

def two_players_main():

    table = ['-' for i in range(9)] # table is a list instead of an array
    player1, player2 = 'X', 'O'
    winner, tie = False, False
    turn = 1
    # Randomly choose player/marker will begin the game
    marker = random.choice([player1, player2])

    while not winner: # while no one winn the game do
        display_board(table) # display the board
        table = player_move(table=table, letter=marker) # player's turn
        print(f'Turn: {turn}, Player {marker}')

        if check_winner(table, marker): # check if there is a winner and display the final board
            display_board(table)
            print(f'Player {marker} Win !!')
            winner = True

        if not check_winner(table, marker) and table_count(table): # check if there is a tie and display the final board
            display_board(table)
            print('Tie')
            tie = True

        marker = change_turn(turn, marker)
        turn = turn + 1



