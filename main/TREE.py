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




root = Node(12)
root.insertNode(6)
root.insertNode(14)
root.insertNode(3)
root.insertNode(4)
root.insertNode(31)
root.insertNode(15)
#root.printTree()
root.inOrderTraversal(root)

