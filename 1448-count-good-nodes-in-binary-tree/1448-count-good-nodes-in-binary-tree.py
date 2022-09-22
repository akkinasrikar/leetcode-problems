# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=1
    
    def goodNodes(self, root: TreeNode) -> int:
        m=root.val
        self.check(root.left,m)
        self.check(root.right,m)
        return self.res
    def check(self,node,n):
        if not node: return
        if node.val>=n:
            self.res += 1
            n=node.val
        self.check(node.left,n)
        self.check(node.right,n)
        return
        
        