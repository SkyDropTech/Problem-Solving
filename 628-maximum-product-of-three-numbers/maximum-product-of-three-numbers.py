class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        n=len(nums)
        nums.sort()
        maxi1=nums[-1]*nums[-2]*nums[-3] 
        maxi2=nums[0]*nums[1]*max(nums)
        return max(maxi1,maxi2)

        
            
