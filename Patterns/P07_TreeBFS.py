#1. Binary Tree Level Order Traversal (easy)
#https://leetcode.com/problems/binary-tree-level-order-traversal/
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

    def levelOrder(self, root):
        if root is None:
            return root
        queue = []
        return_list = []
        queue.append(root)
        while len(queue) > 0:
            ans = []
            l = len(queue)
            for x in range(l):
                node = queue.pop(0)
                ans.append(node.data)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            return_list.append(ans)
        return return_list

#2. Binary Tree Reverse Level Order Traversal (easy)
#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
    def revLevelOrder(self,root):
        if root is None:
            return root
        stack = []
        queue = []
        return_list = []
        queue.append(root)
        while len(queue)>0:
            l = len(queue)
            ans = []
            for x in range(l):
                node = queue.pop(0)
                ans.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            stack.append(ans)
        while stack:
            return_list.append(stack.pop())
        return return_list



root = Node(5)
root.insert(3)
root.insert(2)
root.insert(4)
root.insert(7)
root.insert(6)
root.insert(8)
root.insert(1)

print(root.revLevelOrder(root))