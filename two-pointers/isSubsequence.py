class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == "":
            return True

        sub_index = 0
        res = [False] * len(s)
        
        for i in t:
            if i == s[sub_index]:
                res[sub_index] = True
                if sub_index < len(s) - 1:
                    sub_index += 1

        ans = True
        for i in res:
            ans = ans and i

        return ans
