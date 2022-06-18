"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    def preorder(self, root: 'Node') -> List[int]:
        
        def p(root):
            if not root: return
            res.append(root.val)
            for i in root.children:
                p(i)
        
        res=[]
        p(root)
        return res