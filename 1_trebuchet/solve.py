#!/usr/bin/python3
import argparse
import sys

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("INPUT_FILE", type=str, help="File that contains the corrupted calibration data")
    return parser.parse_args()

def main():
    args = parse()
    valsum = 0
    with open(args.INPUT_FILE, "rb") as infile:
        for line_count, line in enumerate(infile.readlines()):
            nums = ''.join(filter(str.isdigit, line.decode().strip()))
            value = int(nums[0] + nums[-1])
            valsum += value
            print(f"Parsed value {value} from line {line_count + 1}")
    print(f"\nSum: {valsum}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
