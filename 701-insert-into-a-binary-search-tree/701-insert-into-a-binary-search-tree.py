# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        temp=root
        def insert(node):
            if node is None: return TreeNode(val)
            if node.val<val:
                node.right=insert(node.right)
            else:
                node.left=insert(node.left)
            return node
        insert(root)
        return temp