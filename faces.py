def convert(text):
    """Replaces :) with 🙂 and :( with 🙁."""
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    """Gets user input, converts emoticons to emoji, and prints the result."""
    user_input = input("Enter text: ")
    print(convert(user_input))

if __name__ == "__main__":
    main()
