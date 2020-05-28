from TreeSetup import TreeNode, toBinaryTree, printTree
"""
Given two non-empty binary trees s and t, check whether tree t has exactly the
same structure and node values with a subtree of s. A subtree of s is a tree
consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:

   4
  / \
 1   2

Return true, because t has the same structure and node values with a subtree
of s.

"""


class Solution:
    def checkAll(self, s, t):
        """"""
        if not s and not t:
            return True
        if not t and s:
            return False
        if not s and t:
            return False
        if s.val != t.val:
            return False
        return (self.checkAll(s.left, t.left) and
                self.checkAll(s.right, t.right))

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        Check if a tree is a subtree of another tree
        Args:
            s: binary tree
            t: binary tree (subtree)
        Return:
            True or False
        """
        if not s or not t:
            return False

        if self.checkAll(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


# main
tree1 = toBinaryTree([3, 4, 5, 1, 2])
tree2 = toBinaryTree([4, 1, 2])
printTree(tree1)
printTree(tree2)
sol = Solution()
print(sol.isSubtree(tree1, tree2))
