# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        indict = {}
        for i,val in enumerate(inorder):
            indict[val] = i
        pindex = 0
        return self.construct(0,len(inorder)-1,pindex,indict,preorder)[0] 
    
    def construct(self,start,end,pindex,indict,preorder):
        
        if start>end: return None,pindex
        
        root = TreeNode(preorder[pindex])
        pindex += 1
        index = indict.get(root.val)
        root.left,pindex=self.construct(start,index-1,pindex,indict,preorder)
        root.right,pindex=self.construct(index+1,end,pindex,indict,preorder)

        return root,pindex