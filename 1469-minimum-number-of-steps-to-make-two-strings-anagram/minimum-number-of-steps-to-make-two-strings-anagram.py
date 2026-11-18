class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a=[0]*26 
        b=[0]*26 
        n=len(s)
        for i in range(n):
            a[ord(s[i])-ord("a")]+=1 

        for i in range(n):
            b[ord(t[i])-ord("a")]+=1 
        suum=0
        for i in range(26):
            suum+=abs(a[i]-b[i]) 
        return suum//2

        