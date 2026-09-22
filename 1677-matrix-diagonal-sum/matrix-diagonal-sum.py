class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        suum=0
        for i in range(n):
            for j in range(n):
                if i==j:
                    suum+=mat[i][j]
                    suum+=mat[i][n-1-j] 
        if n%2==1:
            suum-=mat[n//2][n//2]
        return suum