class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        ok=True 
        for i in range(2,n-1):
            num=n 
            res=""
            while num>0:
                rem=num%i
                res+=str(rem)
                num=num//i 
            if res!=res[::-1]:
                ok=False
        if ok:
            return True 
        return False




