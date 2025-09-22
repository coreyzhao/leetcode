class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        my_map = Counter(nums)
        count = 0

        for key in my_map:
            if k == 0:
                if my_map[key] > 1:
                    count += 1
            elif key + k in my_map:
                count += 1

            
        
        return count