class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        r = sum(weights)
        res = 99999999999999
        while l <= r:

            m = (l + r) // 2

            cur_days = 1
            cur_weight = 0
            for w in weights:
                if cur_weight + w > m:
                    cur_weight = 0
                    cur_days += 1

                cur_weight += w

            if cur_days <= days:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res

