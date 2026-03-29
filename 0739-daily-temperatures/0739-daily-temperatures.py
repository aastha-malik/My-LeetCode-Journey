class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        i = 0
        while i < len(temperatures) :
            if len(stack) != 0:
                while len(stack) > 0 :
                    x = stack[-1]
                    if temperatures[x] < temperatures[i]:
                        res[x] = i-x
                        stack.pop()
                    else:
                        break

            stack.append(i)   
            i+=1
        
        return res

