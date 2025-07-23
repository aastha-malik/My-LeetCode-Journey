class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = list(set(sentence))
        s.sort()
        
        alpha = list("abcdefghijklmnopqrstuvwxyz")
        return s == alpha

        