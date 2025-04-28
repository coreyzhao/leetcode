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
            
#att 2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_map = {}

        for i in nums:
            if i in element_map:
                element_map[i] += 1
            else:
                element_map[i] = 1
        max_count = -9999
        max_num = 0

        for i in element_map:
          
            if element_map[i] > max_count:
                max_count = element_map[i]
                max_num = i

        return max_num