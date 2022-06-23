# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists and len(lists) == 0: return None
        while len(lists)>1:
            newlist = []
            for i in range(0,len(lists),2):
                a = lists[i]
                b = lists[i+1] if (i+1)<len(lists) else None
                newlist.append(self.mergetwolist(a,b))
            lists = newlist
        return lists[0]
            
    def mergetwolist(self,a,b):
        dummy = ListNode()
        curr = dummy
        while a and b:
            if a.val<b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next
                
        if a: curr.next=a
        if b: curr.next=b
        return dummy.next
    
    