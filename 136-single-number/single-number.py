class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1 
            else:
                freq[i]+=1 
        max_val=min(freq,key=freq.get)
        return max_val