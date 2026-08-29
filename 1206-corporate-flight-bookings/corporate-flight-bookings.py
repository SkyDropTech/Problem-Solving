class Solution:
    def corpFlightBookings(self, nums: List[List[int]], n: int) -> List[int]:
        l=len(nums)
        arr=[0]*(n+2)
        for i in range(l):
            start=nums[i][0] 
            end=nums[i][1] 
            value=nums[i][2] 
            arr[start]+=value
            arr[end+1]-=value
        le=len(arr)
        arr=arr[1:le-1]
        curr=0
        for i in range(len(arr)):
            curr+=arr[i] 
            arr[i]=curr 
        return arr

