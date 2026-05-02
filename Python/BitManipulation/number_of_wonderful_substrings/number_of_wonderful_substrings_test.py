import unittest

from number_of_wonderful_substrings import Solution


class TestNumberOfWonderfulSubstrings(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def brute_force(self, word: str) -> int:
        total = 0
        for start in range(len(word)):
            freq = [0] * 10
            odd_count = 0
            for end in range(start, len(word)):
                index = ord(word[end]) - ord("a")
                freq[index] += 1
                if freq[index] % 2 == 1:
                    odd_count += 1
                else:
                    odd_count -= 1
                if odd_count <= 1:
                    total += 1
        return total

    def test_example_1(self) -> None:
        self.assertEqual(self.solution.wonderfulSubstrings("aba"), 4)

    def test_example_2(self) -> None:
        self.assertEqual(self.solution.wonderfulSubstrings("aabb"), 9)

    def test_example_3(self) -> None:
        self.assertEqual(self.solution.wonderfulSubstrings("he"), 2)

    def test_single_character(self) -> None:
        self.assertEqual(self.solution.wonderfulSubstrings("a"), 1)

    def test_all_same_character(self) -> None:
        self.assertEqual(self.solution.wonderfulSubstrings("aaaa"), 10)

    def test_mixed_short_string(self) -> None:
        word = "abc"
        self.assertEqual(self.solution.wonderfulSubstrings(word), self.brute_force(word))

    def test_larger_mixed_string(self) -> None:
        word = "aabbcc"
        self.assertEqual(self.solution.wonderfulSubstrings(word), self.brute_force(word))

    def test_repeating_pattern(self) -> None:
        word = "ababa"
        self.assertEqual(self.solution.wonderfulSubstrings(word), self.brute_force(word))


if __name__ == "__main__":
    unittest.main()
