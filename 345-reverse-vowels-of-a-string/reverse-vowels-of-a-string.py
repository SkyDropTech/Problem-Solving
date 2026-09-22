class Solution:
    def reverseVowels(self, s: str) -> str:
        vow=["a","e","o","u","i","A","E","I","O","U"]
        lst=[] 
        for i in s:
            lst.append(i) 
        i=0 
        n=len(lst)
        j=n-1
        while i<j:
            if lst[i] not in vow:
                i+=1 
            elif lst[j] not in vow:
                j-=1 
            else:
                lst[i],lst[j]=lst[j],lst[i]
                i+=1 
                j-=1
        return "".join(lst)
        