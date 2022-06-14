# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node,a,b):
            if not node: return True
            if node.val<=a or node.val>=b: return False
            left=valid(node.left,a,node.val)
            right=valid(node.right,node.val,b)
            return left and right
        
        return valid(root,float(-inf),float(inf))
        