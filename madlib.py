def madlib():
    print("Welcome to Mad Libs! Fill in the blanks.")
    
    noun = input("Enter a noun: car ")
    adjective = input("Enter an adjective: black")
    verb = input("Enter a verb: ride ")
    adverb = input("Enter an adverb: strongly")
    place = input("Enter a place: alabama")
    
    story = f"One day, a {adjective} {noun} decided to {verb} {adverb} at the {place}. It was an unforgettable adventure!"
    
    print("\nHere's your Mad Libs story:")
    print(story)
    
if __name__ == "__main__":
    madlib()