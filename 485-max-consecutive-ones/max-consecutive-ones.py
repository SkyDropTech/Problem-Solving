class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ct=0 
        n=len(nums)
        max_num=0
        for i in range(n):
            if nums[i]==1:
                ct+=1 
                max_num=max(max_num,ct)
            else:
                ct=0 
        return max_num