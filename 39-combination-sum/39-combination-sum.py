class Solution:
    def combinationSum(self, candidates,target):
        res=[]
        candidates.sort()
        self.dfs(candidates,res,[],0,target)
        return res
    
    def dfs(self,nums,res,path,idx,target):
        if target==0: 
            res.append(path)
            return
        for i in range(idx,len(nums)):
            if nums[i]>target: break
            self.dfs(nums,res,path+[nums[i]],i,target-nums[i])