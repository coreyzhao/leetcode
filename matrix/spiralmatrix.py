class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, left = 0,0
        bot = len(matrix)
        right = len(matrix[0])

        res = []

        while (top < bot and left < right):

            for i in range(right - left):
                res.append(matrix[top][left + i])
            top += 1

            for i in range(bot - top):
                res.append(matrix[top + i][right - 1])
            right -= 1 

            if not (top < bot and left < right):
                break 

            for i in range(right - left):
                res.append(matrix[bot - 1][right - 1 - i])
            bot -= 1

            for i in range(bot - top):
                res.append(matrix[bot - 1 - i][left])
            left += 1

        return res