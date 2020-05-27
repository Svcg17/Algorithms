"""
    Determine whether or not the given array contains a duplicate value
    @a: array of integers
    Returns: True or False
"""


def containsDuplicates(a):
    """
    newDict = {}
    for i in a:
        if i in newDict:
            return True
        else:
            newDict[i] = 1
    return False
    """
    if len(set(a)) != len(a):
        return True
    return False
