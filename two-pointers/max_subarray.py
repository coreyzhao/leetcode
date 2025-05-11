class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        max_sum = -999999
        cur_sum = 0
        prefix = 0


        while r < len(nums):
            cur_sum += nums[r]
            max_sum = max(cur_sum, max_sum)
            prefix += nums[r]
            r += 1
            

            if prefix < 0:
                l = r
                cur_sum -= prefix
                prefix = 0

        return max_sum


            

