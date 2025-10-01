class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        my_map = {} # h*t: [hot, hit]

        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]

                if pattern in my_map:
                    my_map[pattern].append(word)
                else:
                    my_map[pattern] = [word]

        q = [beginWord]
        visited = set()
        visited.add(beginWord)
        count = 1

        while (q):
            for i in range(len(q)):
                cur_word = q.pop(0)
                if cur_word == endWord:
                    return count

                for i in range(len(cur_word)):
                    pattern = cur_word[:i] + "*" + cur_word[i + 1:]

                    ls = my_map[pattern]
                    for new_word in ls:
                        if new_word not in visited:
                            q.append(new_word)
                            visited.add(new_word)


            count += 1

        return 0

            
