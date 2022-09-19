#1.Merge Intervals (medium)
#https://leetcode.com/problems/merge-intervals/
def merge(intervals):
    if len(intervals)==0:
        return []
    #intervals.sort()
    intervals = sorted(intervals,key = lambda x: x[0])
    stack = [intervals[0]]
    for current in intervals[1:]:
        if current[0]<=stack[-1][1]:
            stack[-1][1] = max(current[1],stack[-1][1])
        else:
            stack.append(current)
    return stack

#2.Insert Interval (medium)
#https://leetcode.com/problems/insert-interval/

#--------------------------------------------------------------------------------------------
intervals = [[2,6],[1,3],[8,10],[15,18]]
print(merge(intervals))