class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ss="".join(sorted(s1))
        n=len(s1)
        m=len(s2) 
        for i in range(m-n+1):
            res=s2[i:i+n]
            res="".join(sorted(res))
            if res==s1 or res==ss:
                return True 
        return False
