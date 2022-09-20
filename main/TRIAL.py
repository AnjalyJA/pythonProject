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

    def levelOrder(self,root):
        if root is None:
            return root
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
            return_list.append(ans)
        return return_list





root = Node(5)
root.insert(3)
root.insert(2)
root.insert(4)
root.insert(7)
root.insert(6)
root.insert(8)
root.insert(1)

#root.inOrderTraversal(root)
#root.preOrderTraversal(root)
#root.postOrderTraversal(root)
#root.printTree()
#print(root.levelOrder(root))


#anagram
def groupAnagrams(strs):
    result = []

    for s in strs:
        ans = []
        ss = sorted(s)
        ans.append(s)
        i = 0
        while i < len(strs):
            isort = sorted(strs[i])
            if ss == isort:
                ans.append(strs[i])
                strs.pop(i)
        result.append(ans)
    print(result)

def isIsomorphic(s,t):
    mapping_s_t = {}
    mapping_t_s = {}
    for c1,c2 in zip(s,t):
        if c1 not in mapping_s_t and c2 not in mapping_t_s:
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1
        elif mapping_s_t.get(c1)!=c2 and mapping_t_s.get(c2)!=c1:
            return False
    return True

def isSubsequence(s,t):
    while i<len(s) and j<len(t):
        if s[i] == t[j]:
            i += 1
        j += 1




strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#print(groupAnagrams(strs))

if isIsomorphic("egg","bddg"):
    print("yes")
else:
    print("no")