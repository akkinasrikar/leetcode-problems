# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node):
            if node is None or node.next is None : return node
            rest=reverse(node.next)
            node.next.next=node
            node.next=None
            return rest
        #return reverse(head)
        
        if not head: return head
        Prev = head
        Tail = None
        Next = head.next
        while Next:
            Prev.next = Tail
            Tail = Prev
            Prev = Next
            Next = Next.next
        Prev.next = Tail
        return Prev