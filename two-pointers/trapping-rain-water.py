class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxArray = [] # [maxLeft, maxRight]
        for i in range(len(height)):
            maxArray.append([0,0])

        curMaxLeft = 0
        for i in range(1,len(height)):
            curMaxLeft = max(height[i - 1], curMaxLeft)
            maxArray[i][0] = curMaxLeft

        curMaxRight = 0
        for i in range(len(height) - 2, -1, -1):
            curMaxRight = max(height[i + 1], curMaxRight)
            maxArray[i][1] = curMaxRight

        print(maxArray)

        total = 0
        for i, ls in enumerate(maxArray):
            trapped = min(ls[0], ls[1]) - height[i]

            if trapped > 0:
                total += trapped

        return total
