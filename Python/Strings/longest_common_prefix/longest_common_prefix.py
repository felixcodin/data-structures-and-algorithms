from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.element = defaultdict(TrieNode)
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.element[char]
        node.isEndOfWord = True

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        
        trie = Trie()
        for s in strs:
            trie.insert(s)

        node = trie.root
        for c in strs[0]:
            if len(node.element) > 1 or node.isEndOfWord:
                break
            res += c
            node = node.element[c]
        
        return res