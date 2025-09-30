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
    
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        r = len(matrix[0])

        t = 0
        b = len(matrix)

        res = []
        while (t < b or l < r):

            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1

            if t >= b or l >= r:
                break

            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1

            if t >= b or l >= r:
                break

            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1

            if t >= b or l >= r:
                break

            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res