class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        res = []

        n = 0
        while n < len(nums):
            if nums[n] in seen:
                nums.pop(n)
            else:
                seen[nums[n]] = 1
                n += 1


        return len(nums)