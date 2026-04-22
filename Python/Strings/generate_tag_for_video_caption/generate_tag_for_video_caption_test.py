import unittest

from generate_tag_for_video_caption import Solution


class TestGenerateTagForVideoCaption(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_caption(self):
        self.assertEqual(self.solution.generateTag(""), "#")

    def test_only_spaces_caption(self):
        self.assertEqual(self.solution.generateTag("     \t   \n"), "#")

    def test_single_word_lowercase(self):
        self.assertEqual(self.solution.generateTag("hello"), "#hello")

    def test_single_word_uppercase(self):
        self.assertEqual(self.solution.generateTag("HELLO"), "#hello")

    def test_multiple_words_basic(self):
        self.assertEqual(self.solution.generateTag("hello world"), "#helloWorld")

    def test_multiple_spaces_between_words(self):
        self.assertEqual(self.solution.generateTag("hello   world   python"), "#helloWorldPython")

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(self.solution.generateTag("   make tests faster   "), "#makeTestsFaster")

    def test_mixed_case_input(self):
        self.assertEqual(self.solution.generateTag("gENeraTe tAG fOr ViDeO"), "#generateTagForVideo")

    def test_numbers_kept_in_words(self):
        self.assertEqual(self.solution.generateTag("version 2 update 10"), "#version2Update10")

    def test_special_characters_are_kept(self):
        self.assertEqual(self.solution.generateTag("new-feature release!"), "#new-FeatureRelease!")

    def test_tab_and_newline_separators(self):
        self.assertEqual(self.solution.generateTag("one\ttwo\nthree"), "#oneTwoThree")

    def test_exactly_99_chars_after_hash_content(self):
        caption = "a" * 99
        self.assertEqual(self.solution.generateTag(caption), "#" + "a" * 99)

    def test_content_longer_than_99_chars_gets_truncated(self):
        caption = "a" * 150
        self.assertEqual(self.solution.generateTag(caption), "#" + "a" * 99)

    def test_truncation_after_camel_case_conversion(self):
        caption = "word " * 40
        result = self.solution.generateTag(caption)
        self.assertEqual(len(result), 100)
        self.assertTrue(result.startswith("#wordWord"))


if __name__ == "__main__":
    unittest.main()
