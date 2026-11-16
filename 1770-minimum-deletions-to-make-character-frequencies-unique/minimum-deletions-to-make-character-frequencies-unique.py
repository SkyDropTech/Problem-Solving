class Solution:
    def minDeletions(self, s: str) -> int:
        freq={} 
        for i in s:
            freq[i]=freq.get(i,0)+1 
        lst=[] 
        for i in freq:
            lst.append(freq[i])
        
        lst.sort(reverse=True)
        ct=0 
        for i in range(1,len(lst)):
            while lst[i]>=lst[i-1] and lst[i]>0:
                lst[i]-=1 
                ct+=1 
                
        return ct

