import sys
from rps import rps
from guess_number import guess_number

def play_game(name="PlayerOne"):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        player_choice = input(f"\nPlease choose a game: \n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press x to exit the Arcade\n\n")

        if player_choice not in ["1", "2", "x"]:
            print(f"{name}, you must enter 1, 2, or x")
            return play_game()
        
        welcome_back = True

        if player_choice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif player_choice == "2":
             guessnumber = guess_number(name)
             guessnumber()
        else:
            print("Thank you for playing!\n")
            sys.exit("Bye!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()


    play_game(args.name)
    

