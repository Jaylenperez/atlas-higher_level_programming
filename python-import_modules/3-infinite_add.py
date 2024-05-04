#!/usr/bin/python3

import sys


def main():
    argv = sys.argv[1:]
    sum_args = sum(int(arg) for arg in argv)
    print(sum_args)


if __name__ == "__main__":
    main()
