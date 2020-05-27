"""
    Determine there is a pair of numbers (one in a, one in b) that can be added
    to sum v
    @a: Array of integers
    @b: Array of integers
    @v: Integer sum
    Return: True or False
"""


def sumOfTwo(a, b, v):
    newSet = set(abs(i - v) for i in a)
    newDict = {}
    b.extend(newSet)
    return len(set(b)) != len(b)
