"""
    Calculates the sum of all the sums gotten from querying nums
    Args:
        @nums: array of integers to sum according to queries indexes
        @queries: 2d array of integers containing a pair of indexes
    Return: An integer of the sums modulo 10^9 + 7
"""


def sumInRange(nums, queries):
    newDict = {}
    init = nums[0]
    total = 0
    newDict[0] = nums[0]
    for i in range(1, len(nums)):
        init = init + nums[i]
        newDict[i] = init
    for q in queries:
        if q[0] > 0:
            total = total + (newDict[q[1]] - newDict[q[0] - 1])
        else:
            total = total + newDict[q[1]]
    return (total % 1000000007)
