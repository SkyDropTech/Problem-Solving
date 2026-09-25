class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        seen=list(sorted(nums)) 
        n=len(seen)
        return seen[n-k]