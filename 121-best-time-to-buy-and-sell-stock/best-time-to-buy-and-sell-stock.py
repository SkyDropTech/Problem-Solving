class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        n=len(arr)
        i=0 
        j=1
        max_val=0
        while j<n:
            if arr[j]<arr[i]:
                i=j 
            else:
                ans=arr[j]-arr[i]
                max_val=max(max_val,ans)
            j+=1 
        return max_val
        