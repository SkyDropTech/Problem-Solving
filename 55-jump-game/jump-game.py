class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # n=len(nums) 
        # maxi=0 
        # if n==1:
        #     return True
        # else:
        #     for i in range(n-1):
        #         if nums[0]==0:
        #             return False
        #             break
        #         if nums[i]==0:
        #             if maxi-i<=0 and nums[i-1]-nums[i]<2:
        #                 return False
        #         maxi=max(maxi,i+nums[i])
        #         maxi-=1 
 
        #     return True
        n=len(nums) 
        maxi=0 
        for i in range(n):
            if i>maxi:
                return False 
            maxi=max(maxi,i+nums[i]) 
        return True
