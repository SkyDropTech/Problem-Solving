class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr=sum(nums[:k])
        max_num=(curr/k)+0.0000 
        for i in range(len(nums)-k):
            curr=curr+nums[k+i]-nums[i] 
            max_num=max((curr/k)+0.0000,max_num)
        return max_num

