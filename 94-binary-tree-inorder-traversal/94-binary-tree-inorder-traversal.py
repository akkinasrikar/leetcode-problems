# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.values=[]
    def inorderTraversal(self, root):
        self.inorder(root)
        return self.values
    def inorder(self,temp):
        if temp==None:
            return
        
        self.inorder(temp.left)
        self.values.append(temp.val)
        self.inorder(temp.right)
        
        