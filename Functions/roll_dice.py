import random

def roll_dice():
    return random.randint(1, 6)

def play_dice_game():
    print("Welcome to the Dice Rolling Game!")

    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled: {result}")

        if result == 6:
            print("Congratulations! You rolled a 6. You win!\n")
        else:
            print("Try again. Good luck!\n")

        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break

play_dice_game()
