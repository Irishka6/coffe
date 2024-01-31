from get_lines import count_lines
import argparse
import os
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='', nargs='*', type=str)
    args = parser.parse_args()
    count_lines(args.file)


if __name__ == "__main__":
    main()

os.system("python3 get_lines.py --file gvgjvkihbh.txt")
