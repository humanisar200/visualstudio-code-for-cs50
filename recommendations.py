def main():
     difficulty = input("Difficult or casual?")
     players = input("multiplayer or singleplayers?")

     if difficulty == "Difficult":
          if player == "Multiplayer":
                   recommend("pocker")
          elif player == "Single-player":
                  recommend("klondike")
          else:
                print("Enter a valid number of players")
     elif difficulty =="Casual":
           if players =="Multiplayers":
                    recommend("Hearts")
     elif player == "Single-player":
                    recommend("Clock")
     else:
             print("Enter a valid Difficlty")


def recommend(game):
        print("you might like",game)


main()