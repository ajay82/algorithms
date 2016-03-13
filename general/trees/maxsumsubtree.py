import treeutils
from tree import TreeNode

def returnMaxSum(node):
    if node == None:
        return [0, 0]
    leftResult = returnMaxSum(node.getLeftChild())
    rightResult = returnMaxSum(node.getRightChild())
    currentSum = node.getValue() + leftResult[0] + rightResult[0]
    maxSum = max(currentSum, leftResult[1], rightResult[1])
    return [currentSum, maxSum]

if __name__ == '__main__':
    print "max sum subtree"
    node = treeutils.createSampleTree()
    treeutils.printTree(node)
    print "finding max sum"
    print returnMaxSum(node)