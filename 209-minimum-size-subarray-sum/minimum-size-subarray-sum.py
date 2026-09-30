class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0 
        curr_val=0
        max_length=float("inf") 
        left_val=0 
        answer=float("inf")
        right_val=0 
        for right in range(len(nums)):
            curr_val+=nums[right] 
            while curr_val>=target:
                answer=min(answer,right-left+1)
                # if right-left+1<max_length:
                #     max_length=right-left+1 
                #     left_val=left 
                #     right_val=right 
                curr_val-=nums[left] 
                left+=1 
        # return nums[left_val:right_val+1]
        if answer==float("inf"):
            return 0
        else:
            return answer
