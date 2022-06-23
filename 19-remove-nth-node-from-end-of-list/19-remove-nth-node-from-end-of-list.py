# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        
        def getlength(node):
            fast,l=node,0
            while fast and fast.next:
                l += 2
                fast = fast.next.next
            return l+bool(fast)
        
        idx = getlength(head)-n
        if idx==0: return head.next
        curr,pos = head,0
        while curr:
            if pos+1==idx:
                curr.next = curr.next.next
                return head
            curr = curr.next
            pos += 1
        return head