class Solution:
    def numIdenticalPairs(self, nums):
        #Bad Apporach because it is using 0(n^2) so we will solve using hashmap
        freq={}
        ans=0          
        for x in nums:
            ans+=freq.get(x,0) 
            freq[x]=freq.get(x,0)+1 
        return ans

        # count = 0

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1

        # return count