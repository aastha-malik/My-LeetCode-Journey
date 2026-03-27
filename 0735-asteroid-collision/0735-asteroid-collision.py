class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = len(asteroids) - 1
        while i > 0:
            x = asteroids[i]
            y = asteroids[i-1]
            if x<0 and y>0: # condition for collision 
                if abs(x) == abs(y): #remove both
                    asteroids.pop(i-1)
                    asteroids.pop(i-1)
                    if i >= len(asteroids):
                        i = len(asteroids) - 1
                    
                elif abs(x) > abs(y):
                    asteroids.pop(i-1)
                    if i >= len(asteroids):
                        i-=1
                    
                else:
                    asteroids.pop(i)
                    if i >= len(asteroids):
                        i-=1
                    
            else:
                i-=1
        return asteroids