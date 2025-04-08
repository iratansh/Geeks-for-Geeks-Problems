class Solution:
    def maxSubArraySum(self, arr):
        dp = [0] * len(arr)
        dp[0] = arr[0]
        
        for i in range(1, len(arr)):
            dp[i] = max(arr[i], arr[i] + dp[i - 1])
        
        return max(dp)
