# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def ismirror(a,b):
            if not a and not b: return True
            if a and b:
                if a.val==b.val:
                    return ismirror(a.left,b.right) and ismirror(a.right,b.left)
            return False
        
        return ismirror(root,root)