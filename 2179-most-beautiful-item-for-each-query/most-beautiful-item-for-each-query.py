class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        n=len(items) 
        m=len(queries) 
        q=[] 
        maxi=0
        items.sort()
        for index, value in enumerate(queries):
            q.append((value,index)) 
        q.sort()
        ans=[0]*m
        i=0 
        for value,index in q:
            while i<n and items[i][0]<=value:
                maxi=max(maxi,items[i][1])
                i+=1  
            ans[index]=maxi 
        return ans