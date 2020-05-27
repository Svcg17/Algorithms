class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Stack:
    """
        A stack linked list
        Args:
            node: A binary tree node
            next: next node
    """

    def __init__(self, node):
        self.node = node
        self.next = None



