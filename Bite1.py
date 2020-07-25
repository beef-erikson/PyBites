"""
Bite 1. Sum n numbers

    Write a function that can sum up numbers:
        It should receive a list of n numbers.
        If no argument is provided, return sum of numbers 1..100.
        Look closely to the type of the function's default argument ...
"""

def sum_numbers(numbers=None):
    sum = 0
    if numbers == None:
        for x in range(1, 101):
            sum += x
    else:
        for x in numbers:
            sum += x
    return sum
