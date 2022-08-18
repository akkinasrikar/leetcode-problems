# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        top=head
        tail=None
        while head:
            if head.val==0:
                Bool=True
                temp=head.next
                while temp and temp.val!=0:
                    head.val += temp.val
                    temp = temp.next
                    Bool=False
                if Bool==True: break
                head.next=temp
                tail=head
                head=head.next
        if Bool==True:
            tail.next=None
        return top
        
        