# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res=[]
        self.inorder(root)
        self.start=0
        self.end=len(self.res)

    def next(self) -> int:
        temp=self.res[self.start]
        self.start += 1
        return temp
        

    def hasNext(self) -> bool:
        return self.start<self.end
    
    def inorder(self,node):
        if not node: return
        self.inorder(node.left)
        self.res.append(node.val)
        self.inorder(node.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()