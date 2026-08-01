class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        arr=[] 
        k=k%n 
        n=len(nums)
        arr=nums[n-k:]
        for i in range(n-k):
            arr.append(nums[i])
        nums[:]=arr
        return nums
        