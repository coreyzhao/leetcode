class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        for i in range(len(s)):
            seen = []
            counter = i
            count = 0
            
            while True:
                if counter == len(s):
                    max_len = max(count, max_len)
                    break

                if s[counter] in seen:
                    max_len = max(count, max_len)
                    break

                else:
                    count += 1
                    seen.append(s[counter])

                counter += 1
                

        return max(count, max_len)
