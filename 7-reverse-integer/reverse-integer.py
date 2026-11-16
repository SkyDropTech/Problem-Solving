class Solution:
    def reverse(self, x: int) -> int:
        
        res=""
        if x>=0: 
            while x>0:
                ans=x%10 
                x=x//10 
                res+=str(ans)
        else:
            x=abs(x)

            while x>0:
                ans=x%10 
                x=x//10 
                res+=str(ans)
            res="-"+res 

        if res=="" or res=="-" :
            return 0 

        res=int(res) 

        if res<-2**31 or res>2**31-1 :
            return 0 

        return res
            



