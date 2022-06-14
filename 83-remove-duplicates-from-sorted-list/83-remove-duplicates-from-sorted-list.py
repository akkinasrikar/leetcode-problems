# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=set()
        temp=head
        prev=None
        while head:
            if head.val in s: 
                prev.next=head.next
                head=head.next
            else: 
                s.add(head.val)
                prev=head
                head=head.next
        return temp