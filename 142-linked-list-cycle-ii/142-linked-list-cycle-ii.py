# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        slow,fast=head,head
        while slow and fast and fast.next:
            slow,fast=slow.next,fast.next.next
            if slow==fast:
                temp=head
                while temp!=slow:
                    slow,temp=slow.next,temp.next
                return slow
        return None
        