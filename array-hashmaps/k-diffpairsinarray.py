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
    
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        my_map = {}

        res = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i - 1]:
                target = nums[i] - k
                my_map[nums[i]] = 1
                if target in my_map:
                    res += 1
            elif i == 0:
                target = nums[i] - k
                my_map[nums[i]] = 1
                if target in my_map:
                    res += 1

        print(my_map)
        count = []
        if k == 0:
            for i in range(len(nums)):
                if nums[i] not in count:
                    if i > 0 and nums[i] == nums[i - 1]:
                        count.append(nums[i])
            return len(count)

        return res                    
                