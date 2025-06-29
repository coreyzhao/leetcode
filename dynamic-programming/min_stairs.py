class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0] * len(cost)

        dp[0] = cost[0]
        dp[1] = cost[1]

        
        for i in range(2, len(cost)):
            ls = [dp[i - 1], dp[i - 2]]
            min_val = min(dp[i - 1], dp[i - 2])

            dp[i] = min_val + cost[i]

        print(dp)
        n = len(cost)

        return min(dp[n - 1], dp[n - 2])





