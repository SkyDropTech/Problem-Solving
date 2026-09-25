class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        freq={} 
        for i in nums:
            freq[i]=freq.get(i,0)+1 
        lst=[]
        ct=0
        for i in freq:
            if freq[i]==1:
                lst.append(i)
                ct+=1 
            if ct==2:
                break
        return lst 
