class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ""
        num = ""
        result =""
        for i in s:
            if i == "]":
                k = len(stack) - 1
                while stack[k] != "[":
                    ans = stack.pop() + ans
                    k-=1
                stack.pop()
                k = len(stack) - 1

                while len(stack)>0 and stack[k].isdigit():
                    num = stack.pop() + num
                    k-=1
                res = ans * int(num)
                #result += res
                stack.append(res)
                ans = ""
                num = ""
                #return [stack, res, ans, num]

            else:
                stack.append(i)
        return "".join(stack)
        
        