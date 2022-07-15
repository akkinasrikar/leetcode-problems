class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0: return [nums[:]]
        res=[]
        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permuteUnique(nums)
            for p in perms:
                p.append(n)
                if p not in res: res.append(p)
            nums.append(n)
        return res