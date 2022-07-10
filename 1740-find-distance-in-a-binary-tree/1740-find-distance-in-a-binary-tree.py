# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        def dfs(node):
            if not node or node.val==p or node.val==q: return node
            left,right=(dfs(node.left),dfs(node.right))
            return node if left and right else left or right
        
        def distance(target,source):
            if not target: return float("inf")
            if target.val==source: return 0
            return 1+min(distance(target.left,source),distance(target.right,source))
        
        lca=dfs(root)
        return distance(lca,p)+distance(lca,q)