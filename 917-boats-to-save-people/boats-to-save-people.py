class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() 
        n=len(people)
        ct=0 
        i=0 
        j=n-1 
        while i<=j:
            if i==j and (people[i]<=limit or people[j]<=limit):
                ct+=1 
                break 
            if people[i]+people[j]<=limit:
                ct+=1 
                i+=1 
            else:
                if people[j]<=limit:
                    ct+=1 
            j-=1 
        return ct
                
            
