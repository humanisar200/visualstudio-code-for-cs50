SHOWS = [
    "Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    "Spongebob Squareparents",
    "Pineas and ferb",
    "Kim Possible",
    "Jimy Neutron",
    "the proud family"
]


def main():
       cleaned_shows = []
       for show in SHOWS:
              print (show.capitalize())
              print (show.title())
              print (show.strip())
              cleaned_shows.append (show.strip().title())

              print(' '.join(cleaned_shows))


              print(cleaned_shows)


main()