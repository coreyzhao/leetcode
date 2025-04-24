class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        memo = {0: nums[0], 1: max(nums[0], nums[1])}
        def dp(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
                return memo[i]

        return dp(len(nums) - 1)
    
    
#attempt2

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if (len(nums) == 1):
            return nums[0]
        
        if (len(nums) == 2):
            return max(nums[0], nums[1])

        memo = {0: nums[0], 1:max(nums[0], nums[1])}
        for i in range(len(nums)):
            if i in memo:
                continue
            else:
                memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])

        return memo[len(nums) - 1]