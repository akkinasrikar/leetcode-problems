# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1: return head
        a=self.getcount(head,0)
        b=a//k
        res,rem=[],[]
        temp=head
        z=0
        while True:
            res.append(temp)
            for i in range(k-1):
                temp=temp.next
                #print(temp.val)
            x=temp.next
            temp.next=None
            temp=x
            z=z+1
            if z==b:
                rem.append(temp)
                break
        
        result=[]
        for i in res:
            result.append(self.reverse(i))
                

        ans=result.pop(0)
        q=ans
        for i in result:
            while ans.next!=None:
                ans=ans.next
                #print(ans.val)
            ans.next=i
            ans=i
        while ans.next!=None:
                ans=ans.next
        ans.next=rem[0]
        return q
    def reverse(self,node):
        if node is None or node.next is None: return node
        rev=self.reverse(node.next)
        node.next.next=node
        node.next=None
        return rev
                
    def getcount(self,node,c):
        if node==None:
            return c
        else:
            return self.getcount(node.next,c+1)
        
        