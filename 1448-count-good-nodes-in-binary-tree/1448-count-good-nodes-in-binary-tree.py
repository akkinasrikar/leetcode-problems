# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=[1]
        m=root.val
        def check(node,n):
            if not node: return
            if node.val>=n:
                res.append(1)
                n=node.val
            check(node.left,n)
            check(node.right,n)
            return
        check(root.left,m)
        check(root.right,m)
        return sum(res)
        