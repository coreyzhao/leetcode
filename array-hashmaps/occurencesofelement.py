class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        my_map = {} # 1st , occurence
        count = 1
        for i in range(len(nums)):
            if nums[i] == x:
                my_map[count] = i
                count += 1

        res = []
        for i in queries:
            if i in my_map:
                res.append(my_map[i])

            else:
                res.append(-1)

        return res
