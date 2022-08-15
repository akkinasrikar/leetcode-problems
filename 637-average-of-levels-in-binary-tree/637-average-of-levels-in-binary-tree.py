# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        res=[]
        ROOT=[root]
        while ROOT:
            values=[i.val for i in ROOT]
            res.append(sum(values)/len(values))
            temp=[(i.left,i.right) for i in ROOT]
            ROOT=[j for i in temp for j in i if j]
        return res
        