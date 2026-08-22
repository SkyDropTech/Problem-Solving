class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq={} 
        for i in nums:
            freq[i]=freq.get(i,0)+1 
        arr=[]
        for i in freq:
            if freq[i]>1:
                arr.append(i) 
        return arr
