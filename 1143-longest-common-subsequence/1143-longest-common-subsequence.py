class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Concept : Dynamic programming (bottom-up approach)
        # Time : O(l1*l2)
        
        l1,l2 = len(text1),len(text2)
        dp = [[0 for i in range(l2+1)] for j in range(l1+1)]
        for i in range(l1-1,-1,-1):
            for j in range(l2-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]
            
        