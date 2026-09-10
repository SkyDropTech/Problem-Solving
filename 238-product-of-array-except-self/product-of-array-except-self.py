class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ct=nums.count(0)
        arr=[0]*n
        if n==1:
            return num[0]
        
        if ct>1:
            return arr
        pr=1
        for i in nums:
            if i!=0:
                pr*=i
        if ct==1:
            for i in range(n):
                if nums[i]==0:
                    arr[i]=pr 
            return arr 
        for i in range(n):
            arr[i]=pr//nums[i] 
        return arr

