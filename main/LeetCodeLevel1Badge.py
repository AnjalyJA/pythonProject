from numpy import inf
def runningSum(nums):
    runningSum = []
    ele = 0
    for i in nums:
        ele += i
        runningSum.append(ele)
    return runningSum

def pivotIndex(nums):
    start = 0
    end = sum(nums)
    for index, num in enumerate(nums):
        end -= num
        if end == start:
            return index
        start += num
    return -1

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
    i,j = 0,0
    while i<len(s) and j<len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return True if i == len(s) else False


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

def maxProfit(prices):
    minPrice = float(inf)
    maxProfit = 0
    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif prices[i] - minPrice > maxProfit:
            maxProfit = prices[i] - minPrice
    return maxProfit


#https://leetcode.com/problems/running-sum-of-1d-array/
#1480.Running Sum of 1d Array
nums = [1,2,3,4]
print("1.running sum")
print(runningSum(nums))

#https://leetcode.com/problems/find-pivot-index/
#724.Find Pivot Index
print("2.pivot index")
print(pivotIndex([1,7,3,6,5,6]))

#https://leetcode.com/problems/isomorphic-strings/
#3.Isomorphic Strings
print("3.isomorphic string?")
if isIsomorphic("egg","bddg"):
    print("yes")
else:
    print("no")

#https://leetcode.com/problems/is-subsequence/
#4. Is Subsequence
print("4.subsequence?")
if isSubsequence("aec","abcde"):
    print("yes")
else:
    print("no")

#https://leetcode.com/problems/number-of-matching-subsequences/
#4.1 Number of Matching Subsequences
print("4.1.Number of Matching Subsequences")
s = "abcde"
words = ["a","bb","acd","ace"]
print(numMatchingSubseq(s,words))

#https://leetcode.com/problems/merge-two-sorted-lists/
#6.Merge Two Sorted Lists

#https://leetcode.com/problems/middle-of-the-linked-list/
#7.Middle of the Linked List

#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#9.Best Time to Buy and Sell Stock
print("9.Best Time to Buy and Sell Stock")
prices = [7,1,5,3,6,4]
print(maxProfit(prices))

#https://leetcode.com/problems/longest-palindrome/
#10.Longest Palindrome