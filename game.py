import random
def get_positive_int(prompt):
    """
    Prompts the user for a positive integer and reprompts if invalid.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass  # Ignore invalid inputs and re-prompt
        print("Invalid input. Please enter a positive integer.")
def main():
    """
    Runs the guessing game where the user tries to guess a randomly generated
number.
    """
    level = get_positive_int("Level: ")
    target = random.randint(1, level)
    while True:
        guess = get_positive_int("Guess: ")
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break  # Exit when the correct guess is made
if __name__ == "__main__":
    main()