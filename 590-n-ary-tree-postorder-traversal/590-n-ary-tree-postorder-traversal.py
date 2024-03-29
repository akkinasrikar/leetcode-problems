"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        def pdt(node):
            if not node: return
            for i in node.children: pdt(i)
            res.append(node.val)
        
        res=[]
        pdt(root)
        return res