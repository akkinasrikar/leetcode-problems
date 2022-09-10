class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k==0: return 0
        return self.get(prices,k)
    def get(self,p,k):
        buy,sell={},{}
        for i in range(1,k+1):
            buy[i],sell[i]=-9999,0
        for i in range(len(p)):
            for j in range(1,k+1):
                if j==1:
                    buy[j]=max(buy[j],-p[i])
                    sell[j]=max(sell[j],buy[j]+p[i])
                else:
                    buy[j]=max(buy[j],sell[j-1]-p[i])
                    sell[j]=max(sell[j],buy[j]+p[i])
        return sell[k]
        