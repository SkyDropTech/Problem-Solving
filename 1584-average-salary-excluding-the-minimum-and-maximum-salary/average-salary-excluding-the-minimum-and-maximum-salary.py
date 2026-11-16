class Solution:
    def average(self, salery: list[int]) -> float:
        n=len(salery)
        x=n-2
        salery.sort() 
        return sum(salery[1:n-1])/x
        