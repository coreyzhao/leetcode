class Solution:
    def reverseWords(self, s: str) -> str:
        my_ls = []
        words_ls = []
        for char in s:
            if char != " ":
                my_ls.append(char)
            else:
                words_ls.append(''.join(my_ls))
                my_ls = []
            
        words_ls.append(''.join(my_ls))
        words_ls.reverse()
        print(words_ls)
        final_str = ""
        for word in words_ls:
            if word != "":
                final_str += word
                final_str += " "
                
        final_str = final_str[:-1]


        return final_str