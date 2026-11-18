class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        nums=["a"]*n 
        k-=n
        i=n-1
        while i>=0 :
            add=min(k,25) 
            nums[i]=chr(add+97)
            k-=add 
            i-=1 
        return "".join(nums)