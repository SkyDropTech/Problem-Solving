class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st1=set(nums1) 
        st2=set(nums2) 
        return list(st1&st2)