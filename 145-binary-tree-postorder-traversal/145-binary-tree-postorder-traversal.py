# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.values=[]
    def postorderTraversal(self, root):
        self.postorder(root)
        return self.values
    def postorder(self,temp):
        if temp==None:
            return
        
        self.postorder(temp.left)
        self.postorder(temp.right)
        self.values.append(temp.val)
        
        