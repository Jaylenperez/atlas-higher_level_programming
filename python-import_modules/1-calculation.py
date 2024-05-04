#!/usr/bin/python3

def main():
    a = 10
    b = 5

    import calculator_1  # Import calculator_1 within main()

    output = "{} + {} = {}\n".format(a, b, calculator_1.add(a, b))
    output += "{} - {} = {}\n".format(a, b, calculator_1.sub(a, b))
    output += "{} * {} = {}\n".format(a, b, calculator_1.mul(a, b))
    output += "{} / {} = {}".format(a, b, calculator_1.div(a, b))

    print(output, end='')

if __name__ == "__main__":
    main()