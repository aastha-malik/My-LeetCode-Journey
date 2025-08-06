class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        if len(word1) > len(word2):
            l = len(word1)
        else:
            l = len(word2)
        for i in range(l):
            if i < len(word1) and i < len(word2):
                s += word1[i]
                s += word2[i]
            elif i < len(word1) and i >= len(word2):
                s += word1[i]
            elif i >= len(word1) and i < len(word2):
                s += word2[i]
        return s