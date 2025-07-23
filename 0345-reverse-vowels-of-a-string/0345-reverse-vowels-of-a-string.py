class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]
        v = []
        for i in s:
            if i in vowel:
                v.append(i)
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowel:
                s[i] = v[-1]
                v.pop()
        return "".join(s)


        