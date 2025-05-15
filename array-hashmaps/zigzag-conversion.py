class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = []
        jump = (numRows - 1) * 2

        if numRows == 1:
            return s
            
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                while i <= len(s) - 1:
                    res.append(s[i])
                    i += jump
            else:
                mini_jump = jump - 2 * i 
                count = jump
                while i <= len(s) - 1:
                    res.append(s[i])
                    if count != jump:
                        i += count
                        count = jump
                    else:
                        i += mini_jump
                        count -= mini_jump

        return ''.join(res)
                


