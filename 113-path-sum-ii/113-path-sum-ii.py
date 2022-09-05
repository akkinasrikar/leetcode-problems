# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        res=[]
        self.dfs(root,targetSum,[],res)
        return res
    def dfs(self,root,targetSum,path,res):
        if root:
            if not root.left and not root.right and targetSum==root.val:
                path.append(root.val)
                res.append(path)
            self.dfs(root.left,targetSum-root.val,path+[root.val],res)
            self.dfs(root.right,targetSum-root.val,path+[root.val],res)
        