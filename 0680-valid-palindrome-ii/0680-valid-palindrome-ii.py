class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(x, y):
            while x< y:
                if s[x] != s[y] :
                    return False
                else:
                    x += 1
                    y -= 1

            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return palindrome(i+1, j) or palindrome(i, j-1)
            else:
                 i += 1
                 j -= 1
        return True




        # i = 0
        # j = len(s) - 1
        # res = 0
        # while i < len(s) and j > -1:
        #     if s[i] == s[j] :
        #         i += 1
        #         j -= 1
        #         res += 1

        #     elif s[i] == s[j-1]:
        #         s = s[:j] + s[j+1:]
        #         n = 0
        #         for k in range(len(s)):
        #             if s[k] == s[len(s) - k -1]:
        #                 n += 1
        #         return n == len(s)
        #     elif s[i+1] == s[j]:
        #         s = s[:i] + s[i+1:]

        #         n = 0
        #         for k in range(len(s)):
        #             if s[k] == s[len(s) - k -1]:
        #                 n += 1
        #         return n == len(s)

        #     else:
        #         return False
        # return res == len(s)