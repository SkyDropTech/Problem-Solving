class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n=len(s) 
        maxi=0 
        ct=1
        if n==1:
            maxi=1
        for i in range(n-1):
            if (ord(s[i])-ord("a"))+1==(ord(s[i+1])-ord("a")):
                ct+=1
            else:
                ct=1
            maxi=max(ct,maxi) 
        return maxi
