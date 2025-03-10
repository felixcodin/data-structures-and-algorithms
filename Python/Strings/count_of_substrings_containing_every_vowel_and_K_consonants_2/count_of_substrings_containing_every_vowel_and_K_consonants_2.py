#You are given a string word and a non-negative integer k.

#Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

class Solution:
    def isVowel(self, c: str) -> bool:
        return c in {'a', 'e', 'i', 'o', 'u'}

    def atLeastK(self, word: str, k: int) -> int:
        numValidSubstrings = 0
        start = 0
        end = 0

        vowelCount = {}
        consonantCount = 0

        while end < len(word):
            newLetter = word[end]

            if self.isVowel(newLetter):
                vowelCount[newLetter] = 1 + vowelCount.get(newLetter, 0)
            else:
                consonantCount += 1

            while len(vowelCount) == 5 and consonantCount >= k:
                numValidSubstrings += len(word) - end
                startLetter = word[start]
                if self.isVowel(startLetter):
                    vowelCount[startLetter] = (vowelCount.get(startLetter) - 1)
                    if vowelCount.get(startLetter) == 0:
                        vowelCount.pop(startLetter)
                else:
                    consonantCount -= 1
                start += 1
            end += 1
        return numValidSubstrings
    
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.atLeastK(word, k) - self.atLeastK(word, k + 1)