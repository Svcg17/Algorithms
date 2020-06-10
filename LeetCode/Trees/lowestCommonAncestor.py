from TreeSetup import TreeNode, toBinaryTree, printTree
"""lowest common ancestor solution of a binary tree solution"""


class Solution:
    """Solution class"""
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        """finds the lowest common ancestor shared by q and p nodes
        Args:
            root: root node type TreeNode
            p: TreeNode to search
            q: TreeNode to search
        Return:
            A TreeNode representing the LCA of q and p
        """
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left and not right:
            return left
        elif right and not left:
            return right


# main
sol = Solution()
tree = toBinaryTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
printTree(tree)
print("==================")
print(sol.lowestCommonAncestor(tree, TreeNode(5), TreeNode(1)).val)
printTree(tree)
print("==================")
print(sol.lowestCommonAncestor(tree, TreeNode(5), TreeNode(4)).val)
