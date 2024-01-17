import regex as re

pattern = r"(:|;)"
pattern2 = r"( )"


def main():
    with open("input.txt") as f:
        temp = f.read().split("\n")
        lines = [re.sub(pattern, ",", line) for line in temp]
        lines = [re.sub(pattern2, "", line) for line in lines]
        lines = [re.split(",", line) for line in lines]
    valid_games = []
    for line in lines:
        game = re.sub(r"Game", "", line[0])
        valid_games.append(game)
        for each in line:
            try:
                if "red" in each:
                    modified_red = re.sub(r"red", "", each)
                    if int(modified_red) > 12:
                        valid_games.remove(game)

                elif "green" in each:
                    modified_green = re.sub(r"green", "", each)
                    if int(modified_green) > 13:
                        valid_games.remove(game)

                elif "blue" in each:
                    modified_blue = re.sub(r"blue", "", each)
                    if int(modified_blue) > 14:
                        valid_games.remove(game)
            except:
                continue

    # using map() to
    # perform conversion
    map_conversion = list(map(int, valid_games))

    # Printing modified list
    print(sum(map_conversion))


if __name__ == "__main__":
    main()
