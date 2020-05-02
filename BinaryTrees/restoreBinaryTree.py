class StaticIdx():
    """Static integer that will be used as index of preorder array"""
    pIdx = 0


def makeTree(inorder, preorder, inoStart, inoEnd, d, pIdx):
    """Constructs binary tree based on inorder and preorder traversals,
    creating binary tree nodes recursively

    Args:
        inorder: array of integers, inorder traversal of the binary tree
        preorder: array of integers, preorder traversal of the binary tree
        inoStart: integer, starting index of inorder array
        inoEnd: integer, ending index of inorder array
        d: dictionary, value of array: index of array
        pIdx: integer, static index used to access preorder values

    Return:
        the created binary tree node
    """
    if inoStart > inoEnd or StaticIdx.pIdx > len(preorder):
        return None

    currVal = preorder[StaticIdx.pIdx]
    StaticIdx.pIdx += 1
    # make new node with preorder value
    newNode = Tree(currVal)

    # if node has no children
    if inoStart == inoEnd:
        return newNode

    # inorder[preorder's current value]
    iIdx = d[currVal]

    # changing boundaries with iDdx for each recursive call
    newNode.left = makeTree(inorder, preorder, inoStart, iIdx - 1, d, pIdx)
    newNode.right = makeTree(inorder, preorder, iIdx + 1, inoEnd, d, pIdx)

    return newNode


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def restoreBinaryTree(inorder, preorder):
    """Construct a binary tree given its inorder and preorder traversals
    in array form

    Creates a lookup hash table with -> key: value of array
                                        value: index of array
    Calls makeTree function and returns constructed binary tree

    Args:
        inorder: array of integers, inorder traversal of the binary tree
        preorder: array of integers, preorder traversal of the binary tree

    Return: Root node of the constructed binary tree
    """

    d = {}
    pIdx = 0
    for i, j in enumerate(inorder):
        d[j] = i
    return makeTree(inorder, preorder, 0, len(inorder) - 1, d, pIdx)
