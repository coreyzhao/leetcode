class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = {}
        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1

        my_ls = []
        for n in seen:
            if seen[n] > 1:
                my_ls.append(n)

        return my_ls