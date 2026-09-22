class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        arr=[] 
        nums.append(0)
        ct=0 
        for i in nums:

            if i==0:
                arr.append(ct) 
                ct=0 
            else:
                ct+=1
        return max(arr)