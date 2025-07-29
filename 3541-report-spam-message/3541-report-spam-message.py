class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        res = 0
        s = set(bannedWords)
        for i in message:
            if i in s:
                res += 1
            if res == 2:
                return True
        return False