class Solution:
    def calPoints(self, operations: list[str]) -> int:
        arr=[] 
        n=len(operations) 
        for i in range(n):
            if operations[i]=="C":
                arr.pop(-1) 
            elif operations[i]=="D":
                arr.append(arr[-1]*2) 
            elif operations[i]=="+":
                arr.append(arr[-2]+arr[-1])
            else:
                arr.append(int(operations[i]))
        return sum(arr)