#!/usr/bin/python3

import sys


def main():
    argv = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print(f"{num_args} argument:")
        print(f"1: {argv[0]}")
    else:
        print(f"{num_args} arguments:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
