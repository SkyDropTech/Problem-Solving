class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ctt=0
        for i in range(len(arr1)):
            ct=0
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])>d:
                        ct+=1 
            if ct==len(arr2):
                ctt+=1
            
        return ctt