class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
  

        longest = 0
        left = 0
        for right in range(len(nums)):

            while nums[right] - nums[left] > 1:
                left += 1

            if nums[right] - nums[left] == 1:
                longest = max(longest, (right - left) + 1)

        return longest