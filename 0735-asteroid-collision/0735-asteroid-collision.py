class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            if asteroids[i] > 0 :
                stack.append(asteroids[i])
                i+=1
            else:
                survive = True
                while len(stack) > 0 and stack[-1] > 0 :
                    if abs(asteroids[i]) > stack[-1]:
                        stack.pop()       
                    elif abs(asteroids[i]) == stack[-1]:
                        stack.pop()
                        survive = False
                        break
                    else:
                        survive = False
                        break
                if survive:
                    stack.append(asteroids[i])  
                i+=1
        return stack


