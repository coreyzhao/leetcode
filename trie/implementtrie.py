class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curNode = self.root
        for char in word:
            if char in curNode.children:
                curNode = curNode.children[char]
            else:
                newNode = TrieNode()
                curNode.children[char] = newNode
                curNode = newNode
        curNode.isEnd = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for char in word:
            if char in curNode.children:
                curNode = curNode.children[char]
            else:
                return False

        if curNode.isEnd == True:
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for char in prefix:
            if char in curNode.children:
                curNode = curNode.children[char]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)