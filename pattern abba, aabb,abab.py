'''Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false'''
class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False

        pattern_map = {}
        seen_words = set()

        for char, word in zip(pattern, words):
            if char not in pattern_map:
                if word in seen_words:
                    return False
                pattern_map[char] = word
                seen_words.add(word)
            else:
                if pattern_map[char] != word:
                    return False

        return True
