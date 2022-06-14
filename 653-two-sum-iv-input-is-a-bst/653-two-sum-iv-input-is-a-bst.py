# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        s=set()
        def check(node):
            if not node: return False
            diff = k- node.val
            if diff in s: return True
            s.add(node.val)
            return check(node.left) or check(node.right)
        
        return check(root)
        