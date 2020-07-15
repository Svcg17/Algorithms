"""
Reverse Words in a String
Given an input string, reverse the string word by word.

Example:
Input: "the sky is blue"
Output: "blue is sky the"
"""


class Solution:
    """Solution to Reverse words in a string problem"""
    def reverseWords(self, s: str) -> str:
        """Reverses the given string word by word excluding extra spaces"""
        s = s.split()
        return ' '.join(reversed(s))


# testing
sol = Solution()
print(sol.reverseWords('a normal sentence'))
print(sol.reverseWords('sentence  with   spaces'))
print(sol.reverseWords(' '))
