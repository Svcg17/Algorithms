from TreeSetup import TreeNode, toBinaryTree, printTree
from typing import List
"""
Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

"""


class Queue:
    """
    A queue class
    Args:
        node: value of the node type TreeNode
        next: next node
    """
    def __init__(self, node=None, next=None):
        self.node = node
        self.next = next

    def addToQueue(self, node):
        """Add node to queue (from the end)"""
        new = Queue(node)
        curr = self
        while curr.next:
            curr = curr.next
        curr.next = new

    def popQueue(self):
        """Pop from queue (first node)"""
        curr = self
        self = self.next
        curr = None
        return self

    def getLen(self):
        """Get length of queue"""
        i = 0
        while self:
            i += 1
            self = self.next
        return i


class Solution:
    """Solution to level order traversal problem"""
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Level order traversal
        Args:
            root: root node of the tree
        Return:
            2d List of each level
        """
        if not root:
            return None
        queue = Queue(root)
        ret = []

        while queue:
            level = []
            i = 0
            queueSize = queue.getLen()
            while i < queueSize:
                curr = queue.node
                if curr.left:
                    queue.addToQueue(curr.left)
                if curr.right:
                    queue.addToQueue(curr.right)
                level.append(curr.val)
                queue = queue.popQueue()
                i += 1

            ret.append(level)

        return ret


# main
tree = toBinaryTree([3, 9, 20, None, None, 15, 7])
printTree(tree)
sol = Solution()
print(sol.levelOrder(tree))
