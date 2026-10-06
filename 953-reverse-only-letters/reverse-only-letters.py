class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        n=len(s) 
        left=0 
        right=n-1 
        while left<right:
            if not s[left].isalpha():
                left+=1 
                continue
            if not s[right].isalpha():
                right-=1 
                continue
            
            s[left],s[right]=s[right],s[left]
            left+=1 
            right-=1
        return "".join(s)
                