# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l=0
        dct={}
        while head:
            dct[l] = head.val
            l += 1
            head = head.next
        if l==2: return sum(dct.values())
        Max=0
        for i in range(l//2):
            Max=max(Max,dct[i]+dct[l-1-i])
        return Max
            
            
        