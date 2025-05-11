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


#2

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        sub_p = 0
        word_p = 0


        while sub_p < len(s) and word_p < len(t):
            if s[sub_p] == t[word_p]:
                sub_p += 1

            word_p += 1


        return sub_p == len(s)