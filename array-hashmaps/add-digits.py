class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            s = str(num)
            res = 0
            for i in s:
                res += int(i)

            num = res

        return num
