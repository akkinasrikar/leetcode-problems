class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        m=len(nums)//2
        root=TreeNode(nums[m])
        root.left=self.sortedArrayToBST(nums[:m])
        root.right=self.sortedArrayToBST(nums[m+1:])
        return root