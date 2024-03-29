#!/usr/bin/python3
import random

allmsg = ["and is greater than 5", "and is 0", "and is less than 6 and not 0"]

number = random.randint(-10000, 10000)
if number > 0:
    last_digit = int(f"{str(number)[-1]}")
else:
    last_digit = int(f"{str(number)[-1]}") * -1

if last_digit > 5:
    msg = allmsg[0]
elif last_digit == 0:
    msg = allmsg[1]
else:
    msg = allmsg[2]

print(f"Last digit of {number:d} is {last_digit} {msg}")
