class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height) 
        i=0 
        j=n-1 
        max_sum=0
        while i<j:
            a=min(height[j],height[i])
            ans=a*(j-i)
            if height[i]>height[j]:
                j-=1 
            elif height[i]<height[j]:
                i+=1 
            else:
                i+=1 
                j-=1
            max_sum=max(max_sum,ans)
        return max_sum
