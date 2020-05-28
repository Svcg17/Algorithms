from TreeSetup import TreeNode, toBinaryTree, printTree
"""
Given a binary tree, determine if it is a valid binary search tree (BST).
    2
   / \
  1   3

Input: [2,1,3]
Output: true
"""


class Solution:
    """
    Solution to validate binary tree problem
    """
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Args:
            root: root node of the binary tree
        Return: True or False
        """
        stack = []
        prev = float('-inf')
        if not root:
            return True
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True


# main
tree = toBinaryTree([2, 1, 3])
printTree(tree)
sol = Solution()
print(sol.isValidBST(tree))
