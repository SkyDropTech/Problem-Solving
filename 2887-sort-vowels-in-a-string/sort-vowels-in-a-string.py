class Solution:
    def sortVowels(self, s: str) -> str:
        n=len(s) 
        lst=[0]*n 
        res=""
        vowel="AEIOUaeiou"
        for i in range(n):
            if s[i] in vowel:
                res+=s[i] 
        ans="".join(sorted(res))
        for i in range(n):
            if s[i] not in vowel:
                lst[i]=s[i] 
        k=len(lst) 
        l=len(ans) 
        i=j=0
        while i<k and j<l:
            if lst[i]==0:
                lst[i]=ans[j] 
                i+=1 
                j+=1 
            else:
                i+=1 
        return "".join(lst)

        