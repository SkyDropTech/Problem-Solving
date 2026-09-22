class Solution:
    def mySqrt(self, x: int) -> int:
        i=0 
        arr=[]
        while True:
            if i*i<=x:
                arr.append(i)
                i+=1
            else:
                break  
        return (max(arr))
