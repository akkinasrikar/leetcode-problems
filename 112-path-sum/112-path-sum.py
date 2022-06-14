# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def check(node,s):
            if node:
                if node.left is None and node.right is None and node.val==s: return True
                else: return check(node.left,s-node.val) or check(node.right,s-node.val)
            else:
                return False
        return check(root,targetSum)