class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        N = len(s)
        
        res = []
        left = [-1] * N
        right = [-1] * N
        pre = [0]
        

        for i in range(N):
            if s[i] == "|":
                left[i] = i
            else:
                if i > 0:
                    left[i] = left[i - 1]

        for i in range(N-1,-1,-1):
            if s[i] == "|":
                right[i] = i
            else:
                if i < N - 1:
                    right[i] = right[i + 1]

        for i in range(N):
            if s[i] == "*":
                pre.append(pre[-1] + 1)
            else:
                pre.append(pre[-1])

        print(left,right,pre)
        for l, r in queries:
            
            l = right[l]
            r = left[r]

            if l != -1 and r != -1 and l <= r:
                res.append(pre[r + 1] - pre[l])
            else:
                res.append(0)

        return res