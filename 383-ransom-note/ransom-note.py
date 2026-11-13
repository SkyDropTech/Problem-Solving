class Solution:
    def canConstruct(self, a: str, b: str) -> bool:
        a="".join(sorted(a))
        b="".join(sorted(b))
        n=len(a)
        m=len(b)
        i=0 
        j=0 
        while i<n and j<m:
            if a[i]==b[j]:
                i+=1 
                j+=1 
            elif a[i]!=b[j]:
                j+=1
        if i==n:
            return True 
        return False