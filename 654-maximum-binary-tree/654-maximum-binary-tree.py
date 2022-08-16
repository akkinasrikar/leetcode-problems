# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def tree(nums,index):
            if len(nums)>0:
                node=TreeNode(nums[index])
                L=nums[:index]
                R=nums[index+1:]
                if L: node.left=tree(L,L.index(max(L)))
                else: node.left=None
                if R: node.right=tree(R,R.index(max(R)))
                else: node.right=None
                return node
        
        return tree(nums,nums.index(max(nums)))
            
        