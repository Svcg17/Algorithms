from TreeSetup import TreeNode, toBinaryTree, printTree

"""
Kth Smallest Element in a BST
Given a binary search tree, write a function kthSmallest to find the kth
smallest element in it.

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
"""


class Solution:
    """
    Contains two solutions: iterative and recursive methods
    Args:
        k: integer, changes state depending on kthSmallestRecursive
    """
    k = 0

    def findKthInorder(self, root):
        if not root:
            return 0
        ret = self.findKthInorder(root.left)
        if self.k == 0:
            return ret
        self.k -= 1
        if self.k == 0:
            return root.val
        return self.findKthInorder(root.right)

    def kthSmallestRecursive(self, root: TreeNode, k: int) -> int:
        self.k = k
        return self.findKthInorder(root)

    def kthSmallestIterative(self, root: TreeNode, k: int) -> int:
        """Finds the kth smallest element in a binary tree
        Args:
            root: TreeNode binary tree
            k: integer representing the smallest number in root
        Returns:
            The kth TreeNode value
        """
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


# main
tree = toBinaryTree([3, 1, 4, None, 2])
printTree(tree)
sol = Solution()
smallest = sol.kthSmallestIterative(tree, 1)
print(smallest)
