# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        dummy=ListNode(0)
        curreven=dummy
        currodd=head
        tempodd=currodd
        while currodd and currodd.next:
            dummy.next=currodd.next
            dummy=dummy.next
            if currodd.next.next:
                currodd.next=currodd.next.next
            else: break
            currodd=currodd.next
        dummy.next=None
        currodd.next=curreven.next
        return tempodd