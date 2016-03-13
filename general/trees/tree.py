
class TreeNode():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
    def getValue(self):
        return self.value
    
    def setLeftChild(self, left):
        self.left = left
    
    def setRightChild(self, right):
        self.right = right
    
    def getRightChild(self):
        return self.right
        
    def getLeftChild(self):
        return self.left

def main():
    print "I am in the main method"
    testNode()
    
def printTree(node):
    if node == None:
        return
    print node.getValue()
    printTree(node.getLeftChild())
    printTree(node.getRightChild())          
    
def testNode():
    node = TreeNode(5)
    leftNode = TreeNode(3)
    node.setLeftChild(leftNode)
    rightNode = TreeNode(7)
    node.setRightChild(rightNode)
    printTree(node)

if __name__ == '__main__':
   main()