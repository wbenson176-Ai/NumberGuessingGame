
print("==NUMBER GUESSING GAME==\n")
print("Welcome to the Number Guessing Game!")
print("I am thinking of a secret number between 1 and 20.")
print("You have 5 attempts to guess the number correctly.\n")
player_name = input("Enter your name: ")
print(f"Hello, {player_name}! Let's start the game.\n")

secret_number = 7 # The secret number to guess
guess_attempt = 0
max_guess = 5

while guess_attempt < max_guess:
    guess = int(input("Enter your guess (between 1 and 20): "))
    guess_attempt += 1

    if guess < 1 or guess > 20:
        print("Please enter a number between 1 and 20.")
        continue

    if guess < secret_number:
        print(f"Too low! Try again, {guess_attempt} attempts used.\n")
    elif guess > secret_number:
        print(f"Too high! Try again, {guess_attempt} attempts used.\n")
    else:
        print(f"Congratulations, {player_name}! You've guessed the secret number {secret_number} in {guess_attempt} attempts!\n")
        print("Thank you for playing the Number Guessing Game. Goodbye!")
        break
else:
    print(f"Sorry, {player_name}. You've used all your attempts. The secret number was {secret_number}. Better luck next time!")    
