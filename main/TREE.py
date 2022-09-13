#BINARY SEARCH TREE

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insertNode(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertNode(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertNode(data)
        else:
            print("else part")
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    #stack
    def inOrderTraversal(self,root):
        current = root
        stack = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                print(current.data,end = " ")
                current = current.right
            else:
                break

    #recursion
    def preorderTraversal1(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal1(root.left)
            res = res + self.preorderTraversal1(root.right)
        return res

    #stack
    def preOrderTraversal2(self,root):
        nodeStack = []
        nodeStack.append(root)

        while(len(nodeStack)>0):
            node = nodeStack.pop()
            print(node.data, end = " ")
            if node.right is not None:
                nodeStack.append(node.right)
            if node.left is not None:
                nodeStack.append(node.left)









root = Node(12)
root.insertNode(6)
root.insertNode(14)
root.insertNode(3)
root.insertNode(4)
root.insertNode(31)

root.printTree()
root.preOrderTraversal2(root)

