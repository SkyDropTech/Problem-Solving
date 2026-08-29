class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        suum=sum(nums)
        return suum%k