class Solution:
    def trailingZeroes(self, n: int) -> int:
        i=1 
        suum=0
        while 5**i<=n:
            suum+=n//(5**i)
            i+=1 
        return suum
