class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []
        for i in range(n - 2):
            new_row = [0] * (n-2)
            res.append(new_row)


        for i in range(n - 2):
            for j in range(n - 2):

                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        res[i][j] = max(res[i][j], grid[r][c])

        return res

        