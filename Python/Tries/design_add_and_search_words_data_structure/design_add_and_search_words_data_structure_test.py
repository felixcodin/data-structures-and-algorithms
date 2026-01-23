import unittest
from design_add_and_search_words_data_structure import WordDictionary

class TestWordDictionary(unittest.TestCase):
    def setUp(self):
        self.word_dict = WordDictionary()

    def testAddAndSearchSingleWord(self):
        self.word_dict.addWord("bad")
        self.assertTrue(self.word_dict.search("bad"))
        self.assertFalse(self.word_dict.search("dad"))

    def testSearchNonExistentWord(self):
        self.word_dict.addWord("bad")
        self.assertFalse(self.word_dict.search("good"))

    def testSearchWithDotAtEnd(self):
        self.word_dict.addWord("bad")
        self.assertTrue(self.word_dict.search("ba."))

    def testSearchWithDotAtBeginning(self):
        self.word_dict.addWord("bad")
        self.assertTrue(self.word_dict.search(".ad"))

    def testSearchWithDotInMiddle(self):
        self.word_dict.addWord("bad")
        self.assertTrue(self.word_dict.search("b.d"))

    def testSearchAllDots(self):
        self.word_dict.addWord("bad")
        self.assertTrue(self.word_dict.search("..."))
        self.assertFalse(self.word_dict.search("...."))

    def testMultipleWords(self):
        self.word_dict.addWord("bad")
        self.word_dict.addWord("dad")
        self.word_dict.addWord("mad")
        self.assertFalse(self.word_dict.search("pad"))
        self.assertTrue(self.word_dict.search("bad"))
        self.assertTrue(self.word_dict.search(".ad"))
        self.assertTrue(self.word_dict.search("b.."))

    def testSearchPrefixOnly(self):
        self.word_dict.addWord("hello")
        self.assertFalse(self.word_dict.search("hell"))

    def testSearchLongerThanAdded(self):
        self.word_dict.addWord("bad")
        self.assertFalse(self.word_dict.search("badder"))

    def testEmptyDictionary(self):
        self.assertFalse(self.word_dict.search("any"))
        self.assertFalse(self.word_dict.search("."))

    def testSingleCharacterWords(self):
        self.word_dict.addWord("a")
        self.word_dict.addWord("b")
        self.assertTrue(self.word_dict.search("a"))
        self.assertTrue(self.word_dict.search("."))
        self.assertFalse(self.word_dict.search("c"))

    def testWordsWithCommonPrefix(self):
        self.word_dict.addWord("word")
        self.word_dict.addWord("world")
        self.assertTrue(self.word_dict.search("word"))
        self.assertTrue(self.word_dict.search("world"))
        self.assertTrue(self.word_dict.search("wor."))
        self.assertTrue(self.word_dict.search("worl."))

    def testDotMatchesMultipleCharacters(self):
        self.word_dict.addWord("cat")
        self.word_dict.addWord("bat")
        self.word_dict.addWord("rat")
        self.assertTrue(self.word_dict.search(".at"))

    def testMultipleDotsInPattern(self):
        self.word_dict.addWord("hello")
        self.assertTrue(self.word_dict.search("h.ll."))
        self.assertTrue(self.word_dict.search(".e.l."))
        self.assertFalse(self.word_dict.search("h.l."))

    def testLongerWords(self):
        self.word_dict.addWord("programming")
        self.assertTrue(self.word_dict.search("programming"))
        self.assertTrue(self.word_dict.search("pro........"))
        self.assertTrue(self.word_dict.search("...gramming"))
        self.assertFalse(self.word_dict.search("program"))

    def testDuplicateWords(self):
        self.word_dict.addWord("test")
        self.word_dict.addWord("test")
        self.assertTrue(self.word_dict.search("test"))
        self.assertTrue(self.word_dict.search("...."))

    def testDifferentLengthWords(self):
        self.word_dict.addWord("a")
        self.word_dict.addWord("at")
        self.word_dict.addWord("ate")
        self.assertTrue(self.word_dict.search("a"))
        self.assertTrue(self.word_dict.search("at"))
        self.assertTrue(self.word_dict.search("ate"))
        self.assertTrue(self.word_dict.search("."))
        self.assertTrue(self.word_dict.search(".."))
        self.assertTrue(self.word_dict.search("..."))

    def testNoMatchWithDot(self):
        self.word_dict.addWord("abc")
        self.assertFalse(self.word_dict.search(".bc."))
        self.assertFalse(self.word_dict.search(".."))


if __name__ == '__main__':
    unittest.main()