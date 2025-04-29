import random

def play_round(user_score, computer_score):
    """Plays a single round of Rock-Paper-Scissors."""
    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Choose your weapon (rock, paper, or scissors): ").lower()
        if user_choice in choices:
            break
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    return user_score, computer_score

def play_game():
    """Manages multiple rounds of the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user_score, computer_score = play_round(user_score, computer_score)
        print(f"\n--- Current Score ---")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
        print("-----------------------\n")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nThanks for playing!")
    if user_score > computer_score:
        print("Congratulations, you are the overall winner!")
    elif computer_score > user_score:
        print("The computer is the overall winner!")
    else:
        print("It's a tie overall!")

if __name__ == "__main__":
    play_game()