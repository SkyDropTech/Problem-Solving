class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq={} 
        for i in nums1:
            freq[i]=freq.get(i,0)+1 
        arr=[] 
        for i in nums2:
            if i in freq and freq[i]>0:
                arr.append(i) 
                freq[i]-=1 
        return arr