class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        self.dfs(candidates,res,[],0,target)
        return res
    
    def dfs(self,nums,res,path,idx,target):
        if target<=0: 
            if target==0: res.append(path)
            return
        for i in range(idx,len(nums)):
            if i>idx and nums[i]==nums[i-1]: continue
            self.dfs(nums,res,path+[nums[i]],i+1,target-nums[i])
        