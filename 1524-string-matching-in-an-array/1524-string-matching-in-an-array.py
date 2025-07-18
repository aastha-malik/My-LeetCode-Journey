class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = []
        for i in words:
            for j in words:
                if i in j and i != j and i not in arr:
                    arr.append(i)
        return arr