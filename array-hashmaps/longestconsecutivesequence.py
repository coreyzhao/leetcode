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

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numsSet = set(nums)
        maxlen = 0

        for n in numsSet:
            cur = n
            if cur - 1 not in numsSet:
                curlen = 0
                while(cur) in numsSet:
                    curlen += 1
                    cur += 1

                maxlen = max(maxlen, curlen)

        return maxlen

        