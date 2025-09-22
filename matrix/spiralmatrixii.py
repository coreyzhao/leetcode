class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        t, l = 0, 0
        b = n
        r = n
        count = 1

        res = []
        for i in range(n):
            res.append([0] * n)

        while t < b and l < r:
            for i in range(r - l):
                res[t][l + i] = count
                count += 1
            t += 1

            if not (t < b and l < r):
                break

            for i in range(b - t):
                res[t + i][r - 1] = count
                count += 1
            r -= 1

            if not (t < b and l < r):
                break

            for i in range(r - l):
                res[b - 1][r - 1 - i] = count
                count += 1
            b -= 1

            if not (t < b and l < r):
                break

            for i in range(b - t):
                print(count, b - 1 - i)
                res[b - 1 - i][l] = count
                count += 1
            l += 1

        return res
