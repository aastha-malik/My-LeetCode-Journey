class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for i in words:
            arr = i.split(separator)
            for j in arr:
                if j != " " and j != "":
                    result.append(j)
        return result
        

