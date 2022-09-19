#https://leetcode.com/problems/reverse-linked-list/submissions/
#1. Reverse Linked List

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
        current = head
        head = head.next
        current.next = prev
        prev = current
    return prev

def isPalindrome(self, head: ListNode) -> bool:
    print("")
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
    fast, slow = head, prev
    while slow:
        if fast.val != slow.val: return False
        fast, slow = fast.next, slow.next
    return True