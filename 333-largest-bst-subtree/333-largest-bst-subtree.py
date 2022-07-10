# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        @lru_cache(None)
        def dfs(node):
            if not node: return 0,999999,-999999
            LeftNo,LeftMin,LeftMax=dfs(node.left)
            RightNo,RightMin,RightMax=dfs(node.right)
            if LeftMax<node.val<RightMin:
                return LeftNo+RightNo+1,min(LeftMin,node.val),max(RightMax,node.val)
            else: return max(LeftNo,RightNo),float("-inf"),float("inf")
        
        return dfs(root)[0]
        
        
        