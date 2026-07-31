class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        res=""
        for i in range(n):
            res+=str(digits[i])
        num=int(res)+1 
        res=str(num)
        lst=list(map(int, res))
        return lst
