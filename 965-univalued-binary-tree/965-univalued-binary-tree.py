# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        dct={}
    
        def get(node):
            if not node: return
            if node.val in dct: dct[node.val] += 1
            else: dct[node.val] = 1
            get(node.left)
            get(node.right)
        
        get(root)
        r=sum(dct.values())
        for i in dct:
            if dct[i]==r: return True
        return False
        