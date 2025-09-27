class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                cur = stack.pop()
                res[cur] = nums[i]
            stack.append(i)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                cur = stack.pop()
                res[cur] = nums[i]
            stack.append(i)

        return res