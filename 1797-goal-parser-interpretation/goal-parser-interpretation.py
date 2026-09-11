class Solution:
    def interpret(self, nums: str) -> str:
        res="" 
        i=0 
        while i<len(nums):
            if nums[i]=="G":
                res+="G"
                i+=1 
            elif nums[i]=="(" and nums[i+1]==")":
                res+="o"
                i+=2 
            elif nums[i]=="(":
                res+="al"
                i+=4 
        return res
            