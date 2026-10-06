class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        ok=False
        while i*i<=num:
            if i*i==num:
                ok=True 
            i+=1
        if ok:
            return True 
        return False
