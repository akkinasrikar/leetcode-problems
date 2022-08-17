# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
            if not node: return 
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        def construct(nums):
            if not nums: return 
            m=len(nums)//2
            root=TreeNode(nums[m])
            root.left=construct(nums[:m])
            root.right=construct(nums[m+1:])
            return root
        
        res=[]
        inorder(root)
        return construct(res)
        