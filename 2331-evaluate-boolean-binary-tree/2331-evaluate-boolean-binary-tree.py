# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def eval(node):
            if node.left is None and node.right is None:
                if node.val==1: return True
                else: return False
            if node.val==2: return eval(node.left) or eval(node.right)
            else: return eval(node.left) and eval(node.right)
        
        return eval(root)