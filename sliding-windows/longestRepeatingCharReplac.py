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