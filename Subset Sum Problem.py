class Solution:
    def isSubsetSum (self, arr, sum):
        # this looks like a 1D DP problem
        # what should dp[i] be? It should represent whether the sum i is achievable
        dp = [False] * (sum + 1)
        dp[0] = True # since sum 0 is possible by taking 0 items
        for num in arr:
            for s in range(sum, num - 1, -1): # iterate backwards 
                if dp[s - num]:
                    dp[s] = True
        return dp[sum]
        
        
