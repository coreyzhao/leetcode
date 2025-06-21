class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0

            if grid[i][j] != 1:
                return 0

            grid[i][j] = 0
            
            num = 1 + dfs(i + 1,j) + dfs(i - 1,j) + dfs(i, j + 1) + dfs(i, j - 1)

            return num

        max_num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    max_num = max(dfs(i,j), max_num)

        return max_num
        