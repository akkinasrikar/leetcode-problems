# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a,b=0,0
        a=self.getcount(headA,0)
        b=self.getcount(headB,0)
        print(a,b)
        if a>b:
            d=a-b
            return self.find(headA,headB,d)
        else:
            d=b-a
            return self.find(headB,headA,d)
    def find(self,x,y,d):
        for i in range(d):
            x=x.next
        while x!=None:
            if x==y: return x
            else:
                x=x.next
                y=y.next
        return None
    def getcount(self,node,c):
        if node==None:
            return c
        else:
            return self.getcount(node.next,c+1)
        
            