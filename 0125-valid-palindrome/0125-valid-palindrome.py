class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].upper() == s[j].upper():
                    i += 1
                    j -= 1
                else:
                    return False
            elif s[i].isalnum() == False:
                i += 1
            else:
                j -= 1
        return True

        