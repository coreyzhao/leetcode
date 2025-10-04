class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_mp = {}
        for word in strs:
            
            word_list = ''.join(sorted(word))
            if word_list in hash_mp:
                hash_mp[word_list].append(word)
            else:
                
                hash_mp[word_list] = [word]

        final_ls = []
        for key in hash_mp:
            final_ls.append(hash_mp[key])

        return final_ls
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        
        
        for i in range(len(strs)):
            
            count = [0] * 26
            for c in strs[i]:
                index = ord(c) - ord("a")
                count[index] += 1

            if tuple(count) in my_map:
                my_map[tuple(count)] = my_map[tuple(count)] + [strs[i]]
            else:
                my_map[tuple(count)] = [strs[i]]

        res = []
        for key in my_map:
            res.append(my_map[key])

        return res


        print(my_map)

