class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for i in s:
            if i.isalnum() == True  :
                arr.append(i.lower())

        def palindrome(i):
            if i < len(arr):
                if arr[i] != arr[len(arr) - 1-i]:
                    return False
                else:
                    return palindrome(i+1)
            else:
                return True
        
        return palindrome(0)