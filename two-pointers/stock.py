class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        lval = 9999
        r = 1
        rval = 0

        profitmax = 0
        while r < len(prices):
            if prices[r] - prices[l] < 0:
                l = r 
                r = l + 1

            else:
                profitmax = max(prices[r] - prices[l], profitmax)

                r += 1

        return profitmax

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = l + 1
            else:
                cur = prices[r] - prices[l]
                maxProfit = max(maxProfit, cur)

                r += 1

        return maxProfit
            