# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node: return 
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
            
        res=[]
        inorder(root)
        print(res)
        r=99999
        for i in range(1,len(res)):
            r=min(r,abs(res[i]-res[i-1]))
        return r