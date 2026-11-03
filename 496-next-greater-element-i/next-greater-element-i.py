class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n=len(nums1)
        nums2.append(0) 
        m=len(nums2)
        lst=[-1]*n 
        for i in range(n):
            for j in range(m-1):
                if nums1[i]==nums2[j]:
                     for k in range(j+1,m):
                        if nums2[k]>nums1[i]:
                            lst[i]=nums2[k]
                            break
        return lst
                    