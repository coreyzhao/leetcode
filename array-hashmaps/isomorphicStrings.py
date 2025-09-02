class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {} # { char : [[count, i]] }
        hashmap1 = {}

        if len(s) != len(t):
            return false

        count = 0
        count1 = 0
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]].append([count, i])
            
            else:
                hashmap[s[i]] = [[count, i]]
                count += 1
            

        for i in range(len(t)):
            if t[i] in hashmap1:
                hashmap1[t[i]].append([count1, i])

            else:
                hashmap1[t[i]] = [[count1, i]]
                count1 += 1

        print(hashmap.values(), hashmap1.values())
        isIso = list(hashmap.values()) == list(hashmap1.values())
        return isIso


            

