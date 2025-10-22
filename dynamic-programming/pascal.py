class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        

        # 1
        # 11
        # 1 2 1

        dp = [0] * numRows

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1],[1,1]]

        if numRows > 2:
            dp[0] = [1]
            dp[1] = [1,1]
            for r in range(2, numRows):
                cur_row = []
                for i in range(len(dp[r - 1])):
                    print(i)
                    if i > 0:
                        cur_row.append(dp[r-1][i] + dp[r-1][i - 1])

                cur_row.insert(0, 1)
                cur_row.append(1)
                dp[r] = cur_row


        return dp
                