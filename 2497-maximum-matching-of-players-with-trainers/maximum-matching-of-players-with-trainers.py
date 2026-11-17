class Solution:
    def matchPlayersAndTrainers(self, nums: list[int], trainers: list[int]) -> int:
        n=len(nums)
        nums.sort() 
        trainers.sort()
        m=len(trainers)
        i=0
        j=0 
        ct=0
        while i<n and j<m:
            if nums[i]<=trainers[j]:
                ct+=1
                i+=1 
                j+=1 
            else:
                j+=1 
        return ct

        