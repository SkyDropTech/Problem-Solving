class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        freq={} 
        arr=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1 
        for i in freq:
            if freq[i]>1:
                arr.append(i)
        return arr
