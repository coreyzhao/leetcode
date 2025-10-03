class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        maxC = 0
        l = 0
        max_len = 0

        for r in range(len(s)):

            if s[r] in seen:
                seen[s[r]] += 1
            else:
                seen[s[r]] = 1
            maxC = max(maxC, seen[s[r]])
           

            while r - l + 1 - maxC > k:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    seen.pop(s[l])
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len
    
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        my_map = {}
        maxlen = 0
        maxfreq = 0
        l = 0
        for r in range(len(s)):
            windowsize = r - l + 1

            my_map[s[r]] = my_map.get(s[r], 0) + 1
            maxfreq = max(maxfreq, my_map[s[r]])

            while windowsize - maxfreq > k:
                my_map[s[l]] -= 1
                l += 1
                windowsize = r - l + 1

            maxlen = max(windowsize, maxlen)

        

        return maxlen   