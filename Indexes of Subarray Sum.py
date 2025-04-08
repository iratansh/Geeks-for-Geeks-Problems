class Solution:
    def subarraySum(self, arr, target):
        l = 0
        curr_sum = 0
        
        for r in range(len(arr)):
            curr_sum += arr[r]
            
            while curr_sum > target and l <= r:
                curr_sum -= arr[l]
                l += 1
            
            if curr_sum == target:
                return [l + 1, r + 1]

        return [-1]
