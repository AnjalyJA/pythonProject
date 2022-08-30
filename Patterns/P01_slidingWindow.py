
def avgSubArray(arr,k):
    print("#1: avgSubArray")
    result=[]

    for i in range(0,len(arr)-k+1):
      sum=0
      for j in range(i,i+k):
          sum+=arr[j]
      result.append(sum/k)

    return result


def maxSubarraySizeK():
    print("#2: maxSubarraySizeK")

# 1: Find Avg of sub-array
# https://leetcode.com/problems/maximum-average-subarray-i/
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(avgSubArray(arr,k))

# 2: Max subarray of size k
# https://leetcode.com/problems/largest-subarray-length-k/
maxSubarraySizeK()

