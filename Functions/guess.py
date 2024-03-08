import random

def generate_random_number():
    return random.randint(1, 10)

def guess_number(secret_number, user_guess):
    if user_guess == secret_number:
        return "Congratulations! You guessed the correct number!"
    elif user_guess < secret_number:
        return "Too low. Try again."
    else:
        return "Too high. Try again."

def play_number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = generate_random_number()
    user_input = input("Enter your guess (1-10): ")   
    user_guess = int(user_input)
    result = guess_number(secret_number, user_guess)
    print(result)
    if result.startswith("Congratulations"):
        print("Congratulations you won")
    else:
        print("Try Again")
play_number_guessing_game()
