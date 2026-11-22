class Solution:
    def checkString(self, s: str) -> bool:
        n=len(s) 
        ct=1
        ok=True 
        for i in range(n-1):
            if s[i]=="a" and s[i+1]=="b":
                ct-=1 
            if s[i]=="b" and s[i+1]=="a":
                ok=False
        if ct>=0 and ok:
            return True 
        return False
