class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set(sentence)        
        alpha = set("abcdefghijklmnopqrstuvwxyz")
        return s == alpha

        