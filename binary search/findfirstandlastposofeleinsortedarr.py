class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(nums) - 1

        maxright = -1

        while l <= r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1

            else:
                maxright = m
                l = m + 1

        l = 0
        r = len(nums) - 1

        maxleft = -1

        while l <= r:
            m = (l + r) // 2
            print(m, l ,r)

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1

            else:
                maxleft = m
                r = m - 1
                # while (l < r):
                #     m = (l + r) // 2
                #     if nums[m] == target:
                #         maxleft = m
                #     r = m - 1

        return [maxleft, maxright]


                    