#!/usr/bin/python3
import argparse
import re
import sys

RED_THRESHOLD = 12
GREEN_THRESHOLD = 13
BLUE_THRESHOLD = 14

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("INPUT_FILE", type=str, help="File that contains the game data")
    return parser.parse_args()

def main():
    args = parse()
    matching_games = []
    with open(args.INPUT_FILE, "rb") as infile:
        for line_count, line in enumerate(infile.readlines()):
            # Per-game loop
            line = line.decode().rstrip()
            match = re.match(r'^Game (\d+):', line)
            if not match:
                print(f"Failed to parse match ID from line {line_count + 1}")
                return 1
            game_id = int(match.group(1))
            data = line.split(":")[1].split(";")
            maxred = maxblue = maxgreen = 0
            for handfull in data:
                # Per-handfill loop
                points = [i.strip() for i in handfull.split(",")]
                bcount = rcount = gcount = 0
                for point in points:
                    count, color = point.split(" ")
                    count = int(count)
                    if color == "red":
                        rcount = count
                    elif color == "green":
                        gcount = count
                    elif color == "blue":
                        bcount = count
                maxred = max(rcount, maxred)
                maxgreen = max(gcount, maxgreen)
                maxblue = max(bcount, maxblue)
            print(f"Game {game_id} maximums:\n\tred: {maxred}\n\tgreen: {maxgreen}\n\tblue: {maxblue}")
            if maxred <= RED_THRESHOLD and maxgreen <= GREEN_THRESHOLD and maxblue <= BLUE_THRESHOLD:
                matching_games.append(game_id)
    print(f"Matching games: {matching_games}")
    gamesum = 0
    for game_id in matching_games:
        gamesum += game_id
    print(f"Matching game ID sum: {gamesum}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
