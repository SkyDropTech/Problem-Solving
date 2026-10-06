class Solution:
    def flipAndInvertImage(self, im: list[list[int]]) -> list[list[int]]:
        n=len(im) 
        for i in range(n):
            im[i].reverse()
            for j in range(n):
                if im[i][j]==1:
                    im[i][j]=0 
                else:
                    im[i][j]=1
            
        return im
