class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) % 2 == 0:
            n = len(s) // 2
        else:
            n = len(s) // 2 + 1

        for i in range(n):
            temp = s[i]
            s[i] = s[-(i + 1)]
            s[-(i + 1)] = temp



            


        