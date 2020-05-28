"""
Binary Tree structure SetUp
"""


class TreeNode:
    """
    A binary tree class called TreeNode that follows leetcode format
    Args:
        val: value of the node
        left: left node
        right: right node
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printTree(root, space=0):
    """Prints binary tree horizontally
    """
    if (root is None):
        return

    space += 10
    printTree(root.right, space)
    print()
    for i in range(10, space):
        print(end=" ")
    print(root.val)
    printTree(root.left, space)


def toBinaryTree(array):
    """
    Creates a binary tree based on LeetCode's format (array to tree)
    Args:
        array: Array representing binary tree in level order
    Return: root node of the created binary tree
    """
    if array:
        stack = [None if i is None else TreeNode(i) for i in array]
    children = stack[::-1]
    root = children.pop()
    for node in stack:
        if node:
            if children:
                node.left = children.pop()
                node.right = children.pop()
    return root


"""
Pass input array to toBinaryTree to create tree
Solve more leet code problems using this tree
"""
# tree = toBinaryTree([3, 9, 20, None, None, 15, 7])
# printTree(tree)
