class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n=len(s)
        m=len(p)
        arr=[]
        p="".join(sorted(p))
        res=""
        for i in range(n-m+1):
            res+=s[i:i+m]
            res="".join(sorted(res))
            if res==p:
                arr.append(i)
            res=""
        return arr


