class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p = 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p = 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i



        return -1

