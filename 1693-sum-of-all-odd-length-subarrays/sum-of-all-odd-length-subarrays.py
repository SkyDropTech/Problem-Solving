class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        suum=0
        for i in range(n):
            for j in range(1,n-i+1,2):
                x=sum(arr[i:i+j])
                suum+=x
        return suum
                                                                                                                                                                                                           