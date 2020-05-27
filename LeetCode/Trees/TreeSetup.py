"""
Binary Tree structure
"""


class TreeNode:
    """
    A binary tree class called TreeNode that follows leetcode format
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def toBinaryTree(array):
    if array:
        stack = [None if i is None else TreeNode(i) for i in array]


tree = toBinaryTree([3, 9, 20, None, None, 15, 7])
