#BINARY SEARCH TREE

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif self.data < data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inOrderTraversal(self,root):
        print("inOrderTraversal")
        stack = []
        current = root
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.data, end=" ")
                current = current.right
            else:
                break
        print("\n")

    def preOrderTraversal(self,root):
        print("preOrderTraversal")
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            print(node.data, end=" ")
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        print("\n")


    def postOrderTraversal(self,root):
        stack = []
        print("postOrderTraversal")
        while True:
            while root:
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()
            if len(stack)>0:
                if root.right is not None and stack[-1]==root.right:
                    stack.pop()
                    stack.append(root)
                    root = root.right
                else:
                    print(root.data,end=" ")
                    root = None
            else:
                break
        print("\n")


    def printTree(self):

        if self.left is not None:
            self.left.printTree()
        print(self.data, end = " ")
        if self.right is not None:
            self.right.printTree()

root = Node(5)
root.insert(3)
root.insert(2)
root.insert(4)
root.insert(7)
root.insert(6)
root.insert(8)
root.insert(1)

root.inOrderTraversal(root)
root.preOrderTraversal(root)
root.postOrderTraversal(root)
root.printTree()