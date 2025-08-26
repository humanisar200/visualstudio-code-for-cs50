distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def convert(au):
    return au * 149597870700

def main():
    for name, distance in distances.items():
        meters = convert(distance)
        print(f"{name}: {distance} AU is {meters} m")

if __name__ == "__main__":
    main()