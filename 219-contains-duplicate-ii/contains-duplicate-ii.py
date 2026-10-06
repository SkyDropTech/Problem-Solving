class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        freq={} 
        for i,ch in enumerate(nums):
            if ch in freq:
                if abs(i-freq[ch])<=k:
                    return True 
            freq[ch]=i
        return False

