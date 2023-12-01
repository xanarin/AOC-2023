#!/usr/bin/python3
import argparse
import re
import sys

spelled_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
regex = r'^(zero|one|two|three|four|five|six|seven|eight|nine|[0-9])'

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("INPUT_FILE", type=str, help="File that contains the corrupted calibration data")
    return parser.parse_args()

def main():
    args = parse()
    valsum = 0
    with open(args.INPUT_FILE, "rb") as infile:
        for line_count, line in enumerate(infile.readlines()):
            line = line.decode().rstrip()
            numstr = ""
            for i in range(len(line)):
                match = re.match(regex, line[i:])
                if match:
                    digit = match.group(1)
                    if not str.isdigit(digit):
                        digit = str(spelled_digits.index(digit))
                    numstr += digit
            print(f"Parsed value {numstr} from line {line_count + 1}")
            valsum += int(numstr[0] + numstr[-1])
    print(f"\nSum: {valsum}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
