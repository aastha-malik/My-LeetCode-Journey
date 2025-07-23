class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        d = len(s)
        n = s.count(letter) * 100
        res = int(n / d)
        return res
