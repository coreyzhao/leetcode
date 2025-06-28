class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    

class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        pre_last = 1


        for i in range(n - 1):
            temp = pre_last
            pre_last = pre_last + last

            last = temp

        return pre_last
    
    