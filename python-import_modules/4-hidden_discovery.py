#!/usr/bin/python3

import importlib.util
import sys

def main():
    spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    for name in dir(hidden_4):
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    main()
