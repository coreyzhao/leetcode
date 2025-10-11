class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        l = 0
        r = x // 2

        while l <= r:
            m = (l + r) // 2

            curres = m * m

            if curres == x:
                return m

            elif curres < x:
                l = m + 1
            else:
                r = m - 1

        return r