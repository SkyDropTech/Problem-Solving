class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={} 
        for i,ch in enumerate(nums):
            ans=target-ch
            if ans in freq:
                return [freq[ans],i]
            freq[ch]=i