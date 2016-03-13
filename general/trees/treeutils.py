from tree import TreeNode

def createSampleTree():
    node = TreeNode(5)
    leftNode = TreeNode(3)
    node.setLeftChild(leftNode)
    rightNode = TreeNode(7)
    node.setRightChild(rightNode)
    return node

def printTree(node):
    if node == None:
        return
    print node.getValue()
    printTree(node.getLeftChild())
    printTree(node.getRightChild()) 