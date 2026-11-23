class Solution:
    def totalWaviness(self, nums1: int, nums2: int) -> int:
        ct=0
        for i in range(nums1,nums2+1):
            s=str(i) 
            for j in range(1,len(s)-1):
                if s[j]>s[j-1] and s[j]>s[j+1]:
                    ct+=1 
                elif s[j]<s[j-1] and s[j]<s[j+1]:
                    ct+=1

        return ct
