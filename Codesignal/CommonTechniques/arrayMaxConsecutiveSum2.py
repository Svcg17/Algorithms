"""
    Find the maximum sum that can be calculated from one an array's contiguous
    subarrays
    Args:
        @inputArray: An array of integers
    Return: the maximum sum of inputArray's contiguous subarrays
"""


def arrayMaxConsecutiveSum2(inputArray):
    greater = maxSum = inputArray[0]
    for i in range(1, len(inputArray)):
        greater = max(greater + inputArray[i], inputArray[i])
        maxSum = max(maxSum, greater)
    return maxSum
