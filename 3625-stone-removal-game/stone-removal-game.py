class Solution:
    def canAliceWin(self, n: int) -> bool:
        s=False
        x=10
        while n>=x or x>=0:
            if x%2==0 and n>=x:
                s=True 
            elif x%2!=0 and n>=x:
                s=False
            n=n-x
            x-=1
        return s
