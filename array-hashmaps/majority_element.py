class Solution:
    #commit
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}

        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

        for i in seen:
            if seen[i] > len(nums)/2:
                return i