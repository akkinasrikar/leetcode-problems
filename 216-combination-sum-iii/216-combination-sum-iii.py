class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        nums=[1,2,3,4,5,6,7,8,9]
        self.dfs(nums,res,[],0,n,k)
        return res
    
    def dfs(self,nums,res,path,idx,target,k):
        l=len(path)
        if target<=0: 
            if target==0 and l==k: res.append(path)
            return
        if l>k: return
        for i in range(idx,len(nums)):
            if i>idx and nums[i]==nums[i-1]: continue
            self.dfs(nums,res,path+[nums[i]],i+1,target-nums[i],k)
        