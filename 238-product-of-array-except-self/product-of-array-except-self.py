class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[0]*n
        ct=nums.count(0) 
        if ct>1:
            return arr 
        pr=1 
        for num in nums:
            if num!=0:
                pr*=num 
        if ct==1:
            for i in range(n):
                if nums[i]==0:
                    arr[i]=pr 
            return arr 
        for i in range(n):
            arr[i]=pr//nums[i] 
        return arr





