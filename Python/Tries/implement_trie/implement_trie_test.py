import unittest
from implement_trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def testInsertAndSearchSingleWord(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))

    def testSearchNonExistentWord(self):
        self.trie.insert("apple")
        self.assertFalse(self.trie.search("app"))

    def testSearchPrefixAsWord(self):
        self.trie.insert("apple")
        self.assertFalse(self.trie.search("app"))
        self.assertFalse(self.trie.search("appl"))

    def testStartsWithValidPrefix(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.startsWith("app"))

    def testStartsWithFullWord(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.startsWith("apple"))

    def testStartsWithInvalidPrefix(self):
        self.trie.insert("apple")
        self.assertFalse(self.trie.startsWith("ban"))

    def testMultipleWords(self):
        self.trie.insert("apple")
        self.trie.insert("app")
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))

    def testInsertPrefixThenWord(self):
        self.trie.insert("app")
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.startsWith("app"))

    def testInsertWordThenPrefix(self):
        self.trie.insert("apple")
        self.trie.insert("app")
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("apple"))

    def testEmptyTrie(self):
        self.assertFalse(self.trie.search("word"))
        self.assertFalse(self.trie.startsWith("word"))

    def testSingleCharacterWords(self):
        self.trie.insert("a")
        self.trie.insert("b")
        self.assertTrue(self.trie.search("a"))
        self.assertTrue(self.trie.search("b"))
        self.assertFalse(self.trie.search("c"))

    def testCommonPrefixes(self):
        self.trie.insert("cat")
        self.trie.insert("car")
        self.trie.insert("card")
        self.assertTrue(self.trie.search("cat"))
        self.assertTrue(self.trie.search("car"))
        self.assertTrue(self.trie.search("card"))
        self.assertTrue(self.trie.startsWith("ca"))
        self.assertFalse(self.trie.search("ca"))

    def testLongWord(self):
        word = "abcdefghijklmnopqrstuvwxyz"
        self.trie.insert(word)
        self.assertTrue(self.trie.search(word))
        self.assertTrue(self.trie.startsWith("abcdef"))

    def testDifferentBranches(self):
        self.trie.insert("apple")
        self.trie.insert("banana")
        self.trie.insert("cherry")
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("banana"))
        self.assertTrue(self.trie.search("cherry"))
        self.assertFalse(self.trie.search("app"))
        self.assertFalse(self.trie.search("ban"))

    def testOverlappingWords(self):
        self.trie.insert("test")
        self.trie.insert("testing")
        self.trie.insert("tester")
        self.assertTrue(self.trie.search("test"))
        self.assertTrue(self.trie.search("testing"))
        self.assertTrue(self.trie.search("tester"))
        self.assertTrue(self.trie.startsWith("test"))

    def testDuplicateInsert(self):
        self.trie.insert("word")
        self.trie.insert("word")
        self.assertTrue(self.trie.search("word"))

    def testSearchEmptyString(self):
        self.trie.insert("word")
        self.assertTrue(self.trie.startsWith(""))

    def testInsertEmptyString(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))


if __name__ == '__main__':
    unittest.main()