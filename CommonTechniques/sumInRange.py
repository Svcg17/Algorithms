"""
    Calculates the sum of all the sums gotten from querying nums
    Args:
        @nums: array of integers to sum according to queries indexes
        @queries: 2d array of integers containing a pair of indexes
    Return: An integer of the sums modulo 10^9 + 7
"""
"""
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
"""


def sumInRange(nums, queries):
    newList = [0] * (len(nums) + 1)
    total = 0

    for i in range(len(nums)):
        newList[i + 1] += newList[i] + nums[i]

    for q in queries:
        total += newList[q[1] + 1] - newList[q[0]]

    return total % 1000000007
