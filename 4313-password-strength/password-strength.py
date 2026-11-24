class Solution:
    def passwordStrength(self, password: str) -> int:
        pt3="0123456789"
        pt4="!@#$"
        ct=0
        pas="".join(set(password))
        n=len(set(password))
        for i in range(n):
            if pas[i].islower():
                ct+=1
            elif pas[i].isupper(): 
                ct+=2 
            elif pas[i] in pt3: 
                ct+=3 
            elif pas[i] in pt4: 
                ct+=5 
        return ct