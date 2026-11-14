class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums) 
        mini=float("inf")
        for left in range(n):
            for right in range(left,n):
                val=nums[left:right+1]
                if r>=len(val)>=l:
                    suum=sum(nums[left:right+1])
                    if suum>0:
                        mini=min(mini,suum) 
        if mini!=float("inf"):
            return mini
        return -1
                    



        