class Solution:
    def subsets(self, nums):
        res=[]
        self.dfs(nums,[],res,len(nums))
        return res
    def dfs(self,nums,path,res,l):
        if len(res)==2**l:
            return
        res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:],path+[nums[i]],res,l)