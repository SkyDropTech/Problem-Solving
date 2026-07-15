class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr=sum(nums[:k])
        max_num=curr
        for i in range(k,len(nums)):
            curr=curr+nums[i]-nums[i-k] 
            max_num=max(max_num,curr)
        return max_num/k

