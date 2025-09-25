class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = 99999
        res = 0

        for i, num in enumerate(nums):
            if nums[i - 1] == num and i > 0:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                sub_target = target - num

                if abs(target - (nums[l] + nums[r] + num)) < diff:
                    diff = abs(target - (nums[l] + nums[r] + num))
                    res = nums[l] + nums[r] + num
                if nums[l] + nums[r] <= sub_target:
                    l += 1
                else:
                    r -= 1

        return res
