class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        arr=[]
        arr.append(0)
        suum=0
        for i in range(n):
            suum+=gain[i] 
            arr.append(suum) 
        return max(arr)

