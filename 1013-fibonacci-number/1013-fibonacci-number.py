class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
        
            first = self.fib(n-1)
            second = self.fib(n-2)
                
                
            a = second
            second = first
            first = second + a
            return first        