"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""


class Solution:
    """
    Solution class
    """
    def addDigits(self, num: int) -> int:
        """Repeatedly adds the digits of a number until the sum results
        in one digit
        Args:
            num: integer to use
        Return: the one digit sum"""
        currSum = 0

        while num != 0:
            currSum = currSum + num % 10
            num = num // 10
            if num == 0 and (currSum // 10 != 0):
                num = currSum
                currSum = 0

        return currSum
