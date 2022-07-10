class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if node in (None,p,q): return node
            left,right=(dfs(node.left),dfs(node.right))
            return node if left and right else left or right
        
        return dfs(root)