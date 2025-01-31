import random
import string
def get_positive_int(prompt):
    """
    Prompts the user for a positive integer between 1 and 100.
    """
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value < 100:
                return value
        except ValueError:
            pass
        print("Invalid input. Please enter a number between 1 and 99.")
def generate_password(letters_count, symbols_count, numbers_count, shuffle=False):
    """
    Generates a password based on the given counts of letters, symbols, and
numbers.
    If shuffle=True, the password will be randomized.
    """
    letters = random.choices(string.ascii_letters, k=letters_count)
    symbols = random.choices("!@#$%^&*()", k=symbols_count)
    numbers = random.choices(string.digits, k=numbers_count)
    password_list = letters + symbols + numbers
    if shuffle:
        random.shuffle(password_list)
    return "".join(password_list)
def main():
    """
    Asks the user for password preferences and generates a password.
    """
    print("Welcome to the Password Generator!")
    num_letters = get_positive_int("How many letters would you like in your
password?")
    num_symbols = get_positive_int("How many symbols would you like? ")
    num_numbers = get_positive_int("How many numbers would you like? ")
    easy_password = generate_password(num_letters, num_symbols, num_numbers,
shuffle=False)
    hard_password = generate_password(num_letters, num_symbols, num_numbers,
shuffle=True)
    print(f"Sequential Password: {easy_password}")
    print(f"Shuffled Password: {hard_password}")
if __name__ == "__main__":
    main()