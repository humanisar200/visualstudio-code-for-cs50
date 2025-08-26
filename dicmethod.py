WORDS = {"Pair": 4, "Hair": 4, "Chair": 5}

def main():
    print("Welcome to the Spelling Bee")
    print("Your letters are: A I P C R H G")

    # Create a copy to avoid modifying the original dictionary during iteration
    words_left = WORDS.copy()

    while len(words_left) > 0:
        print(f"{len(words_left)} words left!")
        guess = input("Guess a word: ").strip().capitalize()

        # Check if guess is in dictionary
        if guess in words_left:
            print(f"Correct! '{guess}' is a valid word.")
            del words_left[guess]  # Remove the correctly guessed word
        else:
            print(f"Sorry, '{guess}' is not in the word list or already guessed.")

    print("That's the game! You guessed all the words!")

if __name__ == "__main__":
    main()