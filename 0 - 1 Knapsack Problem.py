class Solution:
    def knapsack(self, W, val, wt):
        # 2D DP problem: dp[i][w] represents the maximum value we can achieve using the first i items with a knapsack of capacity w
        n = len(val)
        dp = [[0] * (W + 1) for _ in range(n + 1)]
        # Base cases already set: dp[0][w] = 0, dp[i][0] = 0
        for i in range(1, n + 1):
            for w in range(1, W + 1):
                if wt[i-1] <= w: # if there is still remaining space to fit the item 
                    dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w - wt[i-1]])
                else: 
                    dp[i][w] = dp[i - 1][w]
        
        return dp[n][W]
        
    
