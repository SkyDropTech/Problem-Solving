class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1) 
        n2=len(word2) 

        lst=[0]*(n1+n2)*2

        i=0 
        j=0
        while i<n1 and j<(n1+n2)*2:
            lst[j]=word1[i] 
            i+=1 
            j+=2 
        k=0 
        m=1
        while k<n2 and m<(n1+n2)*2:
            lst[m]=word2[k] 
            k+=1 
            m+=2 
        
        res=[]
        for i in lst:
            if i!=0:
                res.append(i) 
        return "".join(res)