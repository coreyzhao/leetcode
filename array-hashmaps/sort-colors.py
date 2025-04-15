class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0,0,0]
        for i in nums:
            counts[i] += 1

        red = counts[0]
        white = counts[1]
        blue = counts[2]

        print(red, white, blue)


        for i in range(len(nums)):
            if red > 0:
                nums[i] = 0
                red -= 1
                continue
            if white > 0:
                nums[i] = 1
                white -= 1
                continue
            if blue > 0:
                nums[i] = 2
                blue -= 1
                continue

        """
        Do not return anything, modify nums in-place instead.
        """

        #attempt2
        