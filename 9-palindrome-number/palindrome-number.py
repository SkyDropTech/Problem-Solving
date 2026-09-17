class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x) 
        yy=y[::-1] 
        if y==yy:
            return True 
        return False
