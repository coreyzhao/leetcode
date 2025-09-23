class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def calc(y, rest):
            delta = 0
            for i in range(rows):
                for j in range(cols):

                    if i > rows // 2 and j == cols // 2:
                        delta += (y != grid[i][j])

                    elif i <= rows // 2 and i == j:
                        delta += (y != grid[i][j])

                    elif i <= rows // 2 and i + j == rows - 1:
                        delta += (y != grid[i][j])

                    else:
                        delta += (rest != grid[i][j])

            return delta 

        return min(calc(0,1),calc(0,2),calc(1,2),calc(1,0),calc(2,1),calc(2,0))