class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)

        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return nums.index(max(nums))

        while l < r:
            m = l + ((r - l) // 2)

            left = nums[m - 1] if m - 1 >= 0 else -99999
            right = nums[m + 1] if m + 1 < len(nums) else -99999

            print(m)
            if left < nums[m] and right < nums[m]:
                return m
            
            if left < nums[m]:
                l = m + 1
            else:
                r = m - 1

        return r