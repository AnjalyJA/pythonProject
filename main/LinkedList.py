class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

#https://leetcode.com/problems/reverse-linked-list/submissions/
#1. Reverse Linked List

    def reverseList(self,head):
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev

    def isPalindrome(self, head):
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = slow
        slow = slow.next
        prev.next = None
        while slow:
            slow.next = prev
            prev = slow
            slow = slow.next
        fast = head
        slow = prev
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True

#https://leetcode.com/problems/merge-two-sorted-lists/
#6.Merge Two Sorted Lists
    def mergeTwoList(list1,list2):
        curr = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return dummy.next

    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else:
            return None  # if not (fast and fast.next): return None
        while head != slow:
            head, slow = head.next, slow.next
        return head



list1 = LinkedList()
list1.head = ListNode(1)
n2 = ListNode(2)
list1.head.next = n2
n3 = ListNode(2)
n2.next = n3
n4 = ListNode(1)
n3.next = n4


list1.detectCycle(list1)
'''if isPalindrome(list1.head):
    print("palin")
else:
    print("not palin")'''

#print(type(head))