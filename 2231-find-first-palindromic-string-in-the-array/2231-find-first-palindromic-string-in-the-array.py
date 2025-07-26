class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            l = len(words[i])
            num = 0
            for j in range(l):
            
                if words[i][j] == words[i][l-j-1]:
                    num += 1
            if num == l:
                return words[i]
        return ""
        