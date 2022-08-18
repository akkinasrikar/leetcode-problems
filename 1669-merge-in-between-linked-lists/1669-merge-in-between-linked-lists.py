# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp=list1
        prev=None
        c=(b-a)+1
        while a!=0:
            prev=list1
            list1=list1.next
            a -= 1
        while c!=0:
            list1=list1.next
            c -= 1
        prev.next=list2
        new_prev=None
        while prev:
            new_prev=prev
            prev=prev.next
        new_prev.next=list1
        return temp
            
            