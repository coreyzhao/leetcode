class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = n
        cols = m

        dp = []
        for i in range(rows):
            row = [0] * cols
            dp.append(row)
        
        dp[n - 1][m - 1] = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 or j == m - 1:
                    dp[i][j] = 1

                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]
