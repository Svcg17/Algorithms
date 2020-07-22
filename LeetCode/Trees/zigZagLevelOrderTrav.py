"""
Given a binary tree, return the zigzag level order traversal of its nodes'
values.
(ie, from left to right, then right to left for the next level and alternate
between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
"""

from TreeSetup import TreeNode, toBinaryTree, printTree
from typing import List


class Solution:
    """Solution class"""
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """Returns the zigzag level order traversal or a binary tree
        Args:
            @root: root node of the binary tree
        Returns: A 2d list of each level and its nodes
        """
        zigzag = []
        levIdx = 0

        if not root:
            return zigzag
        queue = [root]

        while queue:
            level = []
            i = 0
            queueLen = len(queue)
            # queueLen represents the number of nodes in each level
            while i < queueLen:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
                i += 1
            if levIdx % 2 == 0:
                zigzag.append(level)
            else:
                zigzag.append(level[::-1])
            levIdx += 1
        return zigzag


# main
tree = toBinaryTree([3, 9, 20, None, None, 15, 7])
printTree(tree)
sol = Solution()
print(sol.zigzagLevelOrder(tree))
print("==================")
tree = toBinaryTree([3, 9, 20, 29, 45, 15, 7])
printTree(tree)
sol = Solution()
print(sol.zigzagLevelOrder(tree))
