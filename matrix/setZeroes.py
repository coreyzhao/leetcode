class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row1 = 1
        col1 = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    print(r,c)
                    if r == 0:
                        row1 = 0
                    else:
                        matrix[r][0] = 0
                    if c == 0:
                        col1 = 0
                    else:
                        matrix[0][c] = 0
        
        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(len(matrix)):
                    matrix[r][c] = 0

        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                for c in range(len(matrix[0])):
                    matrix[r][c] = 0

        if row1 == 0:
            for c in range(len(matrix[0])):
                    matrix[0][c] = 0

        if col1 == 0:
            for r in range(len(matrix)):
                    matrix[r][0] = 0
