class Solution:
    def reverseVowels(self, s: str) -> str:
        char_ls = []
        index_ls = []
        for i, char in enumerate(s):
            if char.lower() in ["a", "e", "i", "o", "u"]:
                char_ls.append(char)
                index_ls.append(i)

        final_str_ls = []
        for i, char in enumerate(s):
            if i in index_ls:
                final_str_ls.append(char_ls.pop())
            else:
                final_str_ls.append(s[i])



        return(''.join(final_str_ls))
