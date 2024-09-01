class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        max_length = 0

        for n in unique:
            if n - 1 not in unique:
                base = n
                length = 1
                while base + 1 in unique:
                    length += 1
                    base += 1
                max_length = max(length, max_length)

        return max_length
