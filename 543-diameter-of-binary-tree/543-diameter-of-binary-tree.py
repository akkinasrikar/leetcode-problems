# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=[]
        self.getnodes(root,res)
        ans=[self.results(i) for i in res]
        return max(ans)
    
    def getnodes(self,node,res):
        if not node: return
        self.getnodes(node.left,res)
        res.append(node)
        self.getnodes(node.right,res)
    
    def results(self,node):
        return self.get(node.left)+self.get(node.right)
    
    @lru_cache(None)
    def get(self,node):
        if not node: return 0
        else:
            return max(1+self.get(node.left),1+self.get(node.right))
        