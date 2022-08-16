"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res=[]
        nodes=[root]
        while nodes and root:
            val=[i.val for i in nodes]
            res.append(val)
            temp=[j for i in nodes for j in i.children if j]
            nodes=temp
        return res