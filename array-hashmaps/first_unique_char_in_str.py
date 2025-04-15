class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = {}

        for i in range(len(s)):
            if s[i] in my_dict:
                my_dict[s[i]][0] += 1

            else:
                my_dict[s[i]] = [1, i]

        for i in my_dict:
            if my_dict[i][0] == 1:
                return my_dict[i][1]

        return -1

        