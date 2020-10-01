print("Let's play best-of-3 Rock, Paper, Scissors.")
player1_name = input("Player 1, please enter your name: ")
player2_name = input("Player 2, please enter your name: ")

def play_RPS(player1_name, player2_name):
    play_further = True
    player1_score = 0
    player2_score = 0
    winning_score = 2
    player1_prompt = "Player 1 move:\n(a) Rock\n(b) Paper\n(c) Scissors\n\n"
    player2_prompt = "Player 2 move:\n(a) Rock\n(b) Paper\n(c) Scissors\n\n"
    turn_counter = 0

    while play_further is True:
        player1_move = input(player1_prompt)
        player2_move = input(player2_prompt)

        if player1_move.lower() == "a" and player2_move.lower() == "b":
            player2_score += 1
            turn_counter += 1
            print(player2_name + " earned the point.\n")
        elif player1_move.lower() == "a" and player2_move.lower() == "c":
            player1_score += 1
            turn_counter += 1
            print(player1_name + " has earned the point.\n")
        elif player1_move.lower() == "b" and player2_move.lower() == "a":
            player1_score += 1
            turn_counter += 1
            print(player1_name + " earned the point.\n")
        elif player1_move.lower() == "b" and player2_move.lower() == "c":
            player2_score += 1
            turn_counter += 1
            print(player2_name + " has earned the point.\n")
        elif player1_move.lower() == "c" and player2_move.lower() == "a":
            player2_score += 1
            turn_counter += 1
            print(player2_name + " has earned the point.\n")
        elif player1_move.lower() == "c" and player2_move.lower() == "b":
            player1_score += 1
            turn_counter += 1
            print(player1_name + " has earned the point.\n")
        else:
            turn_counter += 1
            print("It is a draw.  Try again.\n")

        if player1_score < winning_score and player2_score < winning_score:
            play_further = True
        else:
            play_further = False
            if player1_score > player2_score:
                print(player1_name + " wins " + str(player1_score) + " to " + str(player2_score) + "!  And it only took " + str(
                        turn_counter) + " turns!  Good job!\n")
                desire_to_play = input("Would you like to play again?  Y/N?  ")
                if desire_to_play.lower() == "y":
                    play_further = True
                    player1_score = 0
                    player2_score = 0
                    turn_counter = 0
                else:
                    play_further = False
            else:
                print(player2_name + " wins " + str(player2_score) + " to " + str(player1_score) + "!  And it only took " + str(
                        turn_counter) + " turns!  Good job!\n")
                desire_to_play = input("Would you like to play again?  Y/N?  ")
                if desire_to_play.lower() == "y":
                    play_further = True
                    player1_score = 0
                    player2_score = 0
                    turn_counter = 0
                else:
                    play_further = False

play_RPS(player1_name, player2_name)


