"""
    hasPathWithGivenSum - Find out if there is a root to leaf path
    in the tree where the sum equals s
    Args:
            @t: Binary tree of integers
            @s: an integer
    Return:
            True if there is a path from root to leaf that equals s.
            Otherwise False
"""


def hasPathWithGivenSum(t, s):
    if not t:
        return False
    s = s - t.value
    if not t.right and not t.left:
        return s == 0

    return hasPathWithGivenSum(t.left, s) or hasPathWithGivenSum(t.right, s)
