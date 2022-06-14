# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.values=[]
    def preorderTraversal(self, root):
        self.preorder(root)
        return self.values
    def preorder(self,temp):
        if temp==None:
            return
        
        self.values.append(temp.val)
        self.preorder(temp.left)
        self.preorder(temp.right)
        
        