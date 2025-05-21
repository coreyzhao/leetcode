class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        max_area = 0

        while (l <= r):
            max_area = max( min(height[l], height[r]) * (r - l), max_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area