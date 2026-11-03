class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[] 
        freq={} 
        for num in nums2:
            while stack and num>stack[-1]:
                remove=stack.pop()
                freq[remove]=num
            stack.append(num)
        lst=[]
        for num in nums1:
            if num in freq:
                lst.append(freq[num])
            else:
                lst.append(-1) 
        return lst
