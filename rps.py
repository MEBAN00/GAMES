import sys
import random
from enum import Enum

def rps(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    evil_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal evil_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = input(f"\n{name}, enter... \n1 for Rock, \n2 for Paper, \n3 for scissors:\n \n")
        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, you must enter 1, 2, or 3")
            return play_rps()
        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        
        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '').title()} .")
        print(f"Evil chose {str(RPS(computer)).replace('RPS.', '').title()} .\n")
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal evil_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🥳 {name}, you win"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🥳 {name}, you win"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🥳 {name}, you win"
            elif player == computer:
                return"🙄 Tie game"
            else:
                evil_wins += 1
                return f"😈 Evil wins\nSorry, {name}..."
                
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count:  {game_count}")
        print(f"\n{name} Wins: {player_wins}")
        print(f"\nEvil Wins:  {evil_wins}")

        print("\nPlay again?")
        while True: 
            playagain = input( "\nY for Yes or \nN for No\n")
            if playagain.lower() not in ["y", "n"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("Thank you for playing!\n")
            sys.exit("Bye!")
    return play_rps



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()