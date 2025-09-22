class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        l = 0
        r = len(matrix[0])
        b = len(matrix)

        rows = len(matrix)
        cols = len(matrix[0])

        cur_row = 0
        cur_col = r - 1

        if rows == 1 or cols == 1:
            return True
        for i in range(r):
            cur_row = 0
            cur_col = r - 1 - i
            val = matrix[cur_row][cur_col]
            while (cur_row < rows and cur_col < cols):
                if matrix[cur_row][cur_col] != val:
                    return False
                cur_row += 1
                cur_col += 1

        for j in range(1, b - 1):
            cur_row = j
            cur_col = 0
            val = matrix[cur_row][cur_col]
            while (cur_row < rows and cur_col < cols):
                if matrix[cur_row][cur_col] != val:
                    return False
                cur_row += 1
                cur_col += 1

        return True

                
