class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1

        if s == "":
            return 0

        if len(s) == 1:
            return 1

        q = [] #char
        q.append(s[0])
        max_len = 0
  
        while r < len(s):

            max_len = max(max_len, len(q))

            while s[r] in q:
                q.pop(0)
                l += 1
            


            q.append(s[r])
            r += 1
            
        max_len = max(max_len, len(q))
        return max_len
            





                