class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen = {}
        res = []

        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1

        for i in seen:
            if seen[i] > len(nums)/3:
                res.append(i)

        return res