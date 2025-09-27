class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        res = [-1] * len(nums1)

        my_map = {}
        for i in range(len(nums1)):
            my_map[nums1[i]] = i

        for i in range(len(nums2)):
            n = nums2[i]
            while stack and n > stack[-1]:
                cur = stack.pop()
                if cur in my_map:
                    index = my_map[cur]
                    res[index] = n

            stack.append(n)

        return res