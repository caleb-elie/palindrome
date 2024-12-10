import random

def play_game():
    player1_goals = 0
    player2_goals = 0

    while True:
        player1_score = random.randint(0, 5)
        player2_score = random.randint(0, 5)

        if player1_score > player2_score:
            player1_goals += 1
            print("Player 1 scored a goal!")
        elif player2_score > player1_score:
            player2_goals += 1
            print("Player 2 scored a goal!")
        else:
            print("It's a draw!")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "no":
            break

    print("Game Over!")
    print("Player 1 goals:", player1_goals)
    print("Player 2 goals:", player2_goals)

play_game()
