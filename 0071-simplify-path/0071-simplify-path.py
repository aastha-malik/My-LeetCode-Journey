class Solution:
    def simplifyPath(self, path: str) -> str:
        curr_dir = "."
        parent_dir = ".."
        s = path.split("/")
        while "" in s:
            s.remove("")
        
        stack = []
        i = 0
        while i < len(s):
            if s[i] == curr_dir:
                i+=1
            elif s[i] == parent_dir:
                if len(stack) != 0:
                    stack.pop()
                i+=1
            else:
                stack.append(s[i])
                i+=1
        res = "/".join(stack)
        return "/"+res

        