class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s) 
        lst=[0]*n
        vow="aeiou" 
        for i in range(n):
            if s[i] in vow:
                lst[i]=1
        
        suum=0
        for i in range(k):
            suum+=lst[i]
        maxi=suum
        for i in range(n-k):
            suum=suum-lst[i]+lst[k+i] 
            maxi=max(maxi,suum) 
        return maxi