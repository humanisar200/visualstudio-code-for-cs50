WORDS = {"Pair" : 4, "Hair" : 4, "Chair" : 5}


def main():
    print("welcome to the spelling Bee")
    print("your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input ("Guess a word")