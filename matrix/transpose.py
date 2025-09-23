class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []

        for j in range(cols):
            new_row = []

            for i in range(rows):
                
                new_row.append(matrix[i][j])
            res.append(new_row)

        return res
    
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        res = []
        for i in range(cols):
            res.append([0] *  rows)

        for r in range(rows):
            for c in range(cols):
                res[c][r] = matrix[r][c]

        return res
                

        