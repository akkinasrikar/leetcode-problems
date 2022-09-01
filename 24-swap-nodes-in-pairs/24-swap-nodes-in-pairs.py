# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        if head==None:
            return None
        get_nodes=self.Node(head,[])
        l=len(get_nodes)
        if l==1:
            return get_nodes[0]
        k=0
        for i in range(l//2):
            get_nodes[k],get_nodes[k+1]=get_nodes[k+1],get_nodes[k]
            k=k+2
        for i in range(l-1):
            get_nodes[i].next=get_nodes[i+1]
        get_nodes[-1].next=None
        return get_nodes[0]
    
    def Node(self,node,res):
        if node != None:
            res.append(node)
            self.Node(node.next,res)
        return res
        