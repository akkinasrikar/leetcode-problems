# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        a=[float("inf")]
        b=[float("inf")]
        def find(node):
            if not node: return
            if node.val<=a[0]: a[0]=node.val
            elif node.val<=b[0]: b[0]=node.val
            find(node.left)
            find(node.right)
        find(root)
        return b[0] if b[0]!=float("inf") else -1
        