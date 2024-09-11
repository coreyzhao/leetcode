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