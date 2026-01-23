# LeetCode 211. Design Add and Search Words Data Structure

class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.is_end_of_word = True        

    def search(self, word: str) -> bool:
        def dfs(root: 'WordDictionary', index: int) -> bool:
            if index == len(word):
                return root.is_end_of_word
            c = word[index]
            if c == '.':
                for value in root.children.values():
                    if dfs(value, index + 1):
                        return True
                return False
            else:
                if c not in root.children:
                    return False
                return dfs(root.children[c], index + 1)
        return dfs(self, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)