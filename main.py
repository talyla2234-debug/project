
def play_game():
    player_1 = input("player 1 name? ")
    player_2 = input("player 2 name? ")
    counter = [0,0]
    def player():
        player1 = input("choose between x or o ")
        if player1 == "x":
            player1 = "x"
            player2 = "o"
            print(f" player 1 is {player1}, player 2 is {player2}")
            return player1, player2
        else:
            player1 = "o"
            player2 = "x"
            print(f" player 1 is {player1}, player 2 is {player2}")
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
            player_choice = input("choose between 1-9 ")
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
        for turn in range(9):
            if turn %2 ==0:
                name= player_1
                sign = answers[0]
                a = 0
            else:
                name= player_2
                sign = answers[1]
                a = 1
            choose_move(sign)
            if victory(board_,sign):
                print(f"{name} wins!")
                counter[a] += 1
                return a
            tie = draw()
            if tie:
                print("draws!")
        return counter

    def victory(board_,answers):
        winning = [answers, answers, answers]
        if winning in winner (board_):
            return True
        else:
            return False
    def winner(board_):
        return [board_[0:3],board_[3:6],board_[6::],board_[0::3], board_[1::3],board_[2::3], board_[0::4], board_[0::4],board_[2:7:2]]
    def draw():
        y = 0
        for turn in range(9):
            y = y + 1
        if y == 8 and victory == False:
            print("draws!")
            return True
        return False

    while True:
        board_ = ['1', '2', '3',
                  '4', '5', '6',
                  '7', '8', '9']
        player_picking = player()
        _board_ = board_.copy()
        board_of_game = board(board_)
        answer = player_picking
        end_game(board_of_game , answer)


        #player_selection = player_picking
        print(f"{player_1} have {counter[0]}")
        print(f"{player_2} have {counter[1]}")

play_game()
