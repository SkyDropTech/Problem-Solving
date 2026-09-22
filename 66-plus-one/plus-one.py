class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        keey="".join(map(str,digits))
        x=str(int(keey)+1) 
        return list(map(int,x))