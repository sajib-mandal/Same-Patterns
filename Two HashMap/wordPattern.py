#  290. Word Pattern


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False 
        charToWord = {}
        wordToChar = {}
        for c, w in zip(pattern, words):      # It's easy
            if ((c in charToWord and charToWord[c] != w) or 
                (w in wordToChar and wordToChar[w] != c)):
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True
        
        
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        charToWord = {}
        wordToChar = {}
        for i in range(len(words)):    # Both are same size
            c1, c2 = pattern[i], words[i]
            if ((c1 in charToWord and charToWord[c1] != c2) or
                (c2 in wordToChar and wordToChar[c2] != c1)):
                return False
            charToWord[c1] = c2
            wordToChar[c2] = c1
        return True
