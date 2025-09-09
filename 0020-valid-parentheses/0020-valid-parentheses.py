class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                res.append(i)
            else:
                if len(res) == 0:
                    return False
                if i == ")":
                    if res[-1] == "(":
                        res.pop()
                    else:
                        return False
                elif i == "}":
                    if res[-1] == "{":
                        res.pop()
                    else:
                        return False
                elif i == "]":
                    if res[-1] == "[":
                        res.pop()
                    else:
                        return False
        return len(res) == 0
        
        