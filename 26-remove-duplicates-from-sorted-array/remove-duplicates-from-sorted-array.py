class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1 
        k=len(freq)
        x=len(nums)-k
        new_arr = list(freq) + ["_"] * x
        for i in range(len(nums)):
            nums[i] = new_arr[i]

        return k