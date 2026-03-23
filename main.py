def play_game():
    def player():
        player1 = input("choose between x or o")
        if player1 == "x":
            player1 = "x"
            player2 = "o"
            print(player1, player2)
            return player1, player2
        else:
            player1 = "o"
            player2 = "x"
            print(player1, player2)
            return player1, player2

    player()
    board_ = ['1', '2', '3',
              '4', '5', '6',
              '7', '8', '9']

    def board(current_board):
        print(f"{board_[0]} | {board_[1]} | {board_[2]}")
        print('---+---+---')
        print(f"{board_[3]} | {board_[4]} | {board_[5]}")
        print('---+---+---')
        print(f"{board_[6]} | {board_[7]} | {board_[8]}")
        return current_board
    board(board_)


play_game()
