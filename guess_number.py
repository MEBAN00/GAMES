import sys
import random

def guess_number(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    

    def play_guess_number():
        nonlocal name
        nonlocal player_wins
       

        player_choice = input(f"\n{name}, guess which number I'm thinking of 1, 2, or 3.\n\n")
        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, you must enter 1, 2, or 3")
            return play_guess_number()
        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        
        print(f"\n{name}, you chose {player_choice} .")
        print(f"I was thinking about the number {computer_choice} .\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            
            if player == computer:
                player_wins += 1
                return f"🥳 {name}, you win"
            else:
                return f"😈 Evil wins\nSorry, {name}..."
    
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count:  {game_count}")
        print(f"\n{name} Wins: {player_wins}")
        print(f"\nYour Winning Percentage: {player_wins/game_count:.2%}")

        print("\nPlay again?")
        while True: 
            playagain = input( "\nY for Yes or \nN for No\n")
            if playagain.lower() not in ["y", "n"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print("Thank you for playing!\n")
            sys.exit("Bye!")
    return play_guess_number



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()

    guessnumber = guess_number(args.name)
    guessnumber()
