class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            cur_char = strs[0][i]
            for s in strs:
                if len(s) == i or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res