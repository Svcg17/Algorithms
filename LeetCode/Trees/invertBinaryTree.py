from TreeSetup import TreeNode, toBinaryTree, printTree
"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \\   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \\   / \
9   6 3   1

"""


class Queue:
    """A queue class"""
    def __init__(self, node=None, next=None):
        self.node = node
        self.next = next

    def addToQueue(self, node):
        """add to queue"""
        new = Queue(node)
        curr = self
        while curr.next:
            curr = curr.next
        curr.next = new

    def popQueue(self):
        """pop from queue"""
        curr = self
        self = self.next
        curr = None
        return self


class Solution:
    """Solution"""
    def invertTree(self, root: TreeNode) -> TreeNode:
        """Inverts a binary tree
        Args:
            root: root node of the tree
        Return:
            root node of the inverted tree
        """
        queue = Queue(root)
        if not root:
            return None

        while queue:
            node = queue.node
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                queue.addToQueue(node.left)
            if node.right:
                queue.addToQueue(node.right)
            queue = queue.popQueue()
        return root


# main
tree = toBinaryTree([4,2,7,1,3,6,9])
printTree(tree)
print("==================")
sol = Solution()
printTree(sol.invertTree(tree))
