# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        values,level=[],[root]
        while root and level:
            values.append([node.val for node in level])
            LRpair=[(node.left,node.right) for node in level]
            level=[leaf for lr in LRpair for leaf in lr if leaf]
        return [i[-1] for i in values]
        