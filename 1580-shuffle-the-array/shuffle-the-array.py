class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]: 
        nums1=nums[:n]
        nums2=nums[n:]
        arr=[]
        for i in range(n):
            arr.append(nums1[i])
            arr.append(nums2[i])
        return arr

