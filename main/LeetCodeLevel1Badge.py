#https://leetcode.com/problems/running-sum-of-1d-array/
#1480.Running Sum of 1d Array

#https://leetcode.com/problems/find-pivot-index/
#724.Find Pivot Index

#https://leetcode.com/problems/isomorphic-strings/
#3.Isomorphic Strings
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

#https://leetcode.com/problems/is-subsequence/
#4. Is Subsequence
def isSubsequence(s,t):
    i,j = 0,0
    while i<len(s) and j<len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return True if i == len(s) else False


#https://leetcode.com/problems/number-of-matching-subsequences/
#4.1 Number of Matching Subsequences
def numMatchingSubseq(s,words):
    count = 0
    def isSub(s,t):
        stack = []
        for i in t:
            stack.append(i)
        n = len(s)
        for i in range(n-1,-1,-1):
            if not stack:
                return True
            if stack[-1] == s[i]:
                stack.pop()
        return False

    hashmap = {}
    for word in words:
        if word not in hashmap:
            if isSub(s,word):
                count += 1
                hashmap[word] = True
            else:
                hashmap[word] = False
        else:
            count += 1

    return count

'''if isIsomorphic("egg","bddg"):
    print("yes")
else:
    print("no")

if isSubsequence("aec","abcde"):
    print("yes")
else:
    print("no")'''

s = "abcde"
words = ["a","bb","acd","ace"]
print(numMatchingSubseq(s,words))