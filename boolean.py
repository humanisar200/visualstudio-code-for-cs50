def main():
     difficulty = input("Difficult or casual?")
     if not (difficulty == "Difficult" or difficulty == "Casual"):
            print("Enter a valid Difficlty")
            return

     player = input("Multiplayer or Single-player?")
     if not (players == "Multi-player" or players == "Singlr-player"):
            print("Enter a valid number of players")
            return

     if difficulty == "Difficult" and players == "Multiplayer":
                   recommend("pocker")
     elif  difficulty == "Difficult" and players == "Single-player":
                  recommend("klondike")
     elif difficulty =="Casual" and  players =="Multiplayers":
                    recommend("Hearts")
     else:
                    recommend("Clock")


def recommend(game):
        print("you might like",game)


main()