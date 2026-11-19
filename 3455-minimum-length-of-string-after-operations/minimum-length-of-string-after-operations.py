class Solution:
    def minimumLength(self, nums: str) -> int:
        n=len(nums) 
        freq={} 
        for i in nums:
            freq[i]=freq.get(i,0)+1 
            ct=0
        for i in freq:
            if freq[i]%2==0:
                ct+=2
            else:
                ct+=1
        return ct