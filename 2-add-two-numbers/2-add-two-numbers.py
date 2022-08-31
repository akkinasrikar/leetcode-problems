# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        def helper(node):
            res=[]
            while node:
                res.append(str(node.val))
                node = node.next

            return "".join(res[::-1])
        
        a,b=helper(l1),helper(l2)
        c=str(int(a)+int(b))
        c=list(c)
        r=ListNode(int(c[0]))
        for i in range(1,len(c)):
            r=ListNode(int(c[i]),r)
        return r
    
        
        