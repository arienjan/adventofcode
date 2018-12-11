from blist import *
import operator

def part1(players: int, lastmarble_worth: int) -> int:
    marbles = blist([0])
    scores = {}
    location = 0

    for player in range(1, players+1):
        scores[player] = 0

    for i in range(1, lastmarble_worth+1):
        player = players if (i%players) == 0 else (i%players)

        if i%1000 == 0:
            print(i)

        if i%23 == 0:
            special_location = location-7 if location-7 > 0 else len(marbles) + location-7
            scores[player] += (marbles[special_location]) + i
            del marbles[special_location]
            location = special_location
        else:
            location = 1 if len(marbles)-location==1 else location+2
            marbles.insert(location, i)
    return max(scores.values())

if __name__ == "__main__":

    assert part1(9,25) == 32
    assert part1(10, 1618) == 8317
    assert part1(13, 7999) == 146373
    assert part1(17, 1104) == 2764
    assert part1(21, 6111) == 54718
    assert part1(30, 5807) == 37305

    print(part1(438, 71626))

    print(part1(438, 71626*100))