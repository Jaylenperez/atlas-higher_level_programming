#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Extract the last digit
last_digit = abs(number) % 10

# Determine the message based on the last digit
if last_digit > 5:
    message = "and is greater than 5"
elif last_digit == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"

# Adjust the message for negative numbers
if number < 0:
    message = message.replace("greater than", "less than")

print(f"Last digit of {number} is {last_digit} {message}")
