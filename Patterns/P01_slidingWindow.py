
def avgSubArray1(arr,k):
    print("#1: avgSubArray")
    result=[]

    for i in range(0,len(arr)-k+1):
      sum=0
      for j in range(i,i+k):
          sum+=arr[j]
      result.append(sum/k)

    return result

def avgOfSubarray2(arr,k):
    print("#1: avgSubArray")
    result = []
    windowStart = 0
    windowSum = 0
    for windowEnd in range(0,len(arr)):
        windowSum += arr[windowEnd]

        if(windowEnd>=k-1):
            result.append(windowSum/k)
            windowSum -= arr[windowStart]
            windowStart += 1
    return result


def maxSubarraySizeK():
    print("#2: maxSubarraySizeK")
    maxSum = 0
    windowSum = 0
    windowStart = 0

    for windowEnd in range(0,len(arr)):
        windowSum += arr[windowEnd]

        if(windowEnd>=k-1):
            maxSum = max(windowSum,maxSum)
            windowSum -= arr[windowStart]
            windowStart += 1

    return maxSum


# 1: Find Avg of sub-array
# https://leetcode.com/problems/maximum-average-subarray-i/
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(avgOfSubarray2(arr,k))

# 2: Max subarray of size k
# https://leetcode.com/problems/largest-subarray-length-k/
print(maxSubarraySizeK())

