class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n=len(nums)
        leftsum=0 
        rightsum=0 
        for i in range(n):
            leftsum=sum(nums[:i]) 
            rightsum=sum(nums[i+1:])
            if leftsum==rightsum:
                return i 
                break 
        else:
            return -1