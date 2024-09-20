class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        seen = []

        if len(s) < 3:
            return count
            
        for i in range(3):
            seen.append(s[i])

        if len(set(seen)) == len(seen):
            count += 1

        
        for i in range(3, len(s)):
            seen.pop(0)
            seen.append(s[i])

            if len(set(seen)) == len(seen):
                count += 1


        return count
            


