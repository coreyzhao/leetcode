class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            print(n)
            goal = target - n
            if goal in seen:
                return [seen[goal], i]

            seen[n] = i



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {} # val : index
        i1 = 0
        i2 = 0

        for i in range(len(nums)):
            if (target - nums[i]) in my_dict:
                i1 = my_dict[target - nums[i]]
                i2 = i

            my_dict[nums[i]] = i

        return [i1, i2]

                