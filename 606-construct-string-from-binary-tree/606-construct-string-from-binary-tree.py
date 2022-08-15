# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def construct(node):
            if not node: return ""
            lr=""
            if node.left and node.right:
                lr="("+construct(node.left)+")"+"("+construct(node.right)+")"
            if node.left and not node.right:
                lr="("+construct(node.left)+")"
            if not node.left and node.right:
                lr="()"+"("+construct(node.right)+")"
            return str(node.val)+lr
        
        return construct(root)
        