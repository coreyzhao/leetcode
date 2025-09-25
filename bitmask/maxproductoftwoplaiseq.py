class Solution:
    def maxProduct(self, s: str) -> int:
        N = len(s)
        mymap = {}

        for mask in range(1 << N): # 2 * N
            curStr = ""
            for n in range(N):
                if (1 << n) & mask:
                    curStr += s[N - n - 1]

            if curStr == curStr[::-1]:
                mymap[mask] = len(curStr)

        res = 0
        for key in mymap:
            for key2 in mymap:
                if key & key2 == 0:
                    if mymap[key] * mymap[key2] > res:
                        res = mymap[key] * mymap[key2]

        return res
