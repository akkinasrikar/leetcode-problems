class Solution:
    def trap(self, height: List[int]) -> int:
        l=len(height)
        MIN=[0]*l
        ML,MR=[0]*l,[0]*l
        MAX=0
        for i in range(1,l):
            MAX=max(height[i-1],MAX)
            ML[i]=MAX
        MAX=0
        for i in range(l-2,-1,-1):
            MAX=max(height[i+1],MAX)
            MR[i]=MAX
        res=0
        for i in range(l):
            temp = min(ML[i],MR[i])-height[i]
            if temp>0: res += temp
            else: continue
        return res
                
            
        