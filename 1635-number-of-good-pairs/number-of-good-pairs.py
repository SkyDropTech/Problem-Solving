class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq={} 
        ct=0
        for i in nums:
            if i in freq:
                ct+=freq[i] 
                freq[i]+=1
            else:
                freq[i]=1
        return ct
