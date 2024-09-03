class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mini = 0

        while left <= right:
            mid = left + ((right - left) // 2)
            
            if nums[mid] < mini:
                mini = nums[mid]
            if nums[0] <= nums[len(nums) - 1]:
                return nums[0]
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid] < nums[right]:
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            
            

      
            
            

        return mini