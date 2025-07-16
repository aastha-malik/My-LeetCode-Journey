class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type" :
            ind = 0
        elif ruleKey == "color" :
            ind = 1
        elif ruleKey == "name" :
            ind = 2

        res = 0
        for i in items:
            if i[ind] == ruleValue:
                res += 1

        return res
                


        