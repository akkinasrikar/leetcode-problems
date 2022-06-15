class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l=len(cost)
        @lru_cache(None)
        def dp(idx):
            if idx>=l: return 0
            return min(cost[idx]+dp(idx+1),cost[idx]+dp(idx+2))
        return min(dp(0),dp(1))