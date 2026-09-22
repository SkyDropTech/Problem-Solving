class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        num1=[]
        num2=[] 
        num=[]
        for i in nums:
            if i>=0:
                num1.append(i) 
            else:
                num2.append(i) 
        for i in range(len(num1)):
            num.append(num1[i])
            num.append(num2[i])
        return num

        