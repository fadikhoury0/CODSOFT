import random

def get_user_choice():
    while True:
        user_input = input("Please choose an option from the following: Rock(1), Paper(2), or Scissors(3): ").lower()
        if user_input in ['1', 'rock', '2', 'paper', '3', 'scissors']:
            if user_input in ['1', 'rock']:
                return 1
            elif user_input in ['2', 'paper']:
                return 2
            else:
                return 3
        else:
            print("Invalid choice. Please choose 1 for rock, 2 for paper, or 3 for scissors.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        print(f"You chose: {choices[user_choice]}")
        print(f"Computer chose: {choices[computer_choice]}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            if user_score > computer_score:
                print("Congratulations! You won!")
            elif user_score < computer_score:
                print("Computer wins!")
            else:
                print("It's a tie!")
            print("Thanks for playing!")
            break

play_game()
