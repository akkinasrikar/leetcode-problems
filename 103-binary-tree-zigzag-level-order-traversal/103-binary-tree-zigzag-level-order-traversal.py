# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
      def zigzagLevelOrder(self, root):
            values,level=[],[root]
            l=1
            while root and level:
                if l%2!=0:
                    values.append([node.val for node in level])
                else:
                    z=[node.val for node in level]
                    z.reverse()
                    values.append(z)
                LRpair=[(node.left,node.right) for node in level]
                level=[leaf for lr in LRpair for leaf in lr if leaf]
                l+=1
            return values
        