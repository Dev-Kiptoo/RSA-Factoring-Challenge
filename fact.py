#!/usr/bin/python3
import sys

def factorize(num):
    """ Generate 2 factors for a given number"""
    factor1 = 2
    while num % factor1:
        if factor1 <= num:
            factor1 += 1

    factor2 = num // factor1
    return (factor1, factor2)  # Swap factor1 and factor2

if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

filename = sys.argv[1]

file = open(filename, 'r')
lines = file.readlines()

for line in lines:
    num = int(line.rstrip())
    factor1, factor2 = factorize(num)  # Swap factor1 and factor2
    print(f"{num} = {factor1} * {factor2}")
