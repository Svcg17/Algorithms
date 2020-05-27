"""
    Binary trees are already defined with this interface:
    class Tree(object):
        def __init__(self, x):
            self.value = x
            self.left = None
            self.right = None
"""


def checkBoth(left, right):
    """
    Recursively calls itself to check if two nodes and their children are
    the same.
    Args:
        @left: left node of a binary tree
        @right: right node of a binary tree

    Return:
        True if they match, False if they don't

    """
    if not left and not right:
        return True
    elif left and right:
        if left.value == right.value and \
                checkBoth(left.left, right.right) and \
                checkBoth(left.right, right.left):
            return True
    return False


def isTreeSymmetric(t):
    """
    Checks if root is null or calls checkBoth function with root's left and
    right nodes
    Args:
        @t: root node of binary tree
    Return:
        True or False
    """
    if not t:
        return True
    return checkBoth(t.left, t.right)
