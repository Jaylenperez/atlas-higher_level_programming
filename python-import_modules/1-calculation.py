#!/usr/bin/python3
import calculator_1

a = 10
b = 5

output = f"{a} + {b} = {calculator_1.add(a, b)}\n"
output += f"{a} - {b} = {calculator_1.sub(a, b)}\n"
output += f"{a} * {b} = {calculator_1.mul(a, b)}\n"
output += f"{a} / {b} = {calculator_1.div(a, b)}"

print(output, end='')

