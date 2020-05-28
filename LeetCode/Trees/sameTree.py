from TreeSetup import TreeNode, toBinaryTree, printTree
"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical
and the nodes have the same value.

Example 1:

Input:     1         1
          / \\       / \\
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

"""


class Solution:
    """Solution"""
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """Checks if two binary trees are the same
        Args:
            p: TreeNode tree
            q: TreeNode tree
        Return:
            True or False
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


# main
tree1 = toBinaryTree([1,2,3])
tree2 = toBinaryTree([1,2,3])
sol = Solution()
print(sol.isSameTree(tree1, tree2))
