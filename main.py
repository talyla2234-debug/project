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
    def choose_move(answers):
        while True:
            player_choice = input("choose between 1-9")
            if player_choice.isdigit():
                player_choice = int(player_choice)
                if 1<= player_choice <=9 :
                    if board_[player_choice-1] != "x" and board_[player_choice-1] != "o":
                        board_[player_choice-1] = answers
                        board(board_)
                        return board_
                    else:
                        print("invalid choice")
                        continue
        return player_choice
    def end_game(board_,answers):
        while True:
            player_choice = input("choose between 1-9")
    def victory(board_,player_choice):
        winning = [answers, answers, answers]
        if winning in winner (board_):
            return True
        else:
            return False
    def winner(board_):
        return [board_[0:3],board_[3:6],board_[6::],board_[0::3], board_[1::3],board_[2::3], board_[0::4], board_[1::4],board_[2:6:2]]


play_game()
