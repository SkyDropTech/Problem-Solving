class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n=len(nums) 
        x=n//3 
        lst=[]
        freq={} 
        for i in nums:
            freq[i]=freq.get(i,0)+1 
        for i in freq:
            if freq[i]>x:
                lst.append(i) 
        return lst