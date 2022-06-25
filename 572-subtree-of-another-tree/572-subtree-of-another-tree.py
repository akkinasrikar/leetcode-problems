
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # If t tree is none we instantly have a match
        if t is None:
            return True
        # If t isn't None and S is we don't have a match
        if s is None:
            return False
        # If any of the node values we transverse match t we check for same tree
        if s.val == t.val:
            if self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right):
                return True
        # Recurse if no match s left and right with an "OR" since only need one match
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def is_same_tree(self, s: TreeNode, t: TreeNode) -> bool:
        # If both our none typically leaf nodes we have a match on that Node
        if s is None and t is None:
            return True
        # If one is None and the other has a value we don't have a match
        elif s is None or t is None:
            return False
        # If both values match continue to check if children also match
        if s.val == t.val:
            return self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right)