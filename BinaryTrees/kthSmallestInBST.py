"""
class Tree(object):
  def __init__(self, x):
     self.value = x
     self.left = None
     self.right = None
"""


def kthSmallestInBST(t, k):
    """
        Finds the kth element of a binary search tree
        Implementation of In-order traversal using Morris Traversal
        Args:
            @root: root node of a binary tree
            @k: an integer
        Returns:
            The value of the kth node of the binary search tree
    """
    counter = 0
    current = t
    while(current is not None):
        # a node that can be threaded has been reached, print
        if current.left is None:
            counter += 1
            if counter == k:
                return current.value
            current = current.right
        else:
            pre = current.left
            # Get the rightmost child
            while(pre.right is not None and pre.right != current):
                pre = pre.right

            # rightmost child will be threaded to current
            if(pre.right is None):
                pre.right = current
                current = current.left
            # Otherwise, the node is threaded, print and fix it back
            else:
                pre.right = None
                counter += 1
                if counter == k:
                    return current.value
                current = current.right
