class Solution:
    def rob(self,nums:List[int])->int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        nums1=nums[1:]
        nums2=nums[:-1]
        m=n-1
        dp1=[0]*m
        dp2=[0]*m
        dp1[0]=nums1[0]
        dp2[0]=nums2[0]
        dp1[1]=max(nums1[0],nums1[1])
        dp2[1]=max(nums2[0],nums2[1])
        for i in range(2,m):
            dp1[i]=max(dp1[i-1],dp1[i-2]+nums1[i])
            dp2[i]=max(dp2[i-1],dp2[i-2]+nums2[i])
        return max(dp1[m-1],dp2[m-1])