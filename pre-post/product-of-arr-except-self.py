class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = 1
        post = 1

        for i in range(len(nums)):
            print(i)
            res.append(pre)
            pre = pre * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            
            res[i] = res[i] * post
            post = post * nums[i]

        return res

            
            