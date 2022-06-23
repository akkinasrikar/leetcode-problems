# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res=[root.val]
        def SUM(node):
            if not node: return 0
            left,right=SUM(node.left),SUM(node.right)
            res[0]=max(res[0],node.val+left+right)
            return max(node.val+left,node.val+right,0)
        
        SUM(root)
        return res[0]
        