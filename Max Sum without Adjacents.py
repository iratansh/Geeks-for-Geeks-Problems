#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr):
		# 1D DP question
		# table[i] represnts the the max sum using elements from arr[0...i] with no 2 summed elements that are adjacent in arr?
		# then return table[-1]?
		dp = [0] * len(arr)
		dp[0] = arr[0] # base case = arr[0] since theres only 1 elemnt considered for the sum
		for i in range(1, len(arr)):
		    dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])
		   
        return dp[-1]
		
