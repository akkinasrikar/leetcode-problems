"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        hashmap={}
        def clone(node):
            if node in hashmap: return hashmap[node]
            copy=Node(node.val)
            hashmap[node]=copy
            for neigh in node.neighbors:
                copy.neighbors.append(clone(neigh))
            return copy
        return clone(node)
        
        