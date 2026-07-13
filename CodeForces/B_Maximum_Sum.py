t=int(input())
res=""
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort() 
        
  
   
# t=int(input())
# res=""
# for _ in range(t):
#     n,k=map(int,input().split())
#     a=list(map(int,input().split()))
#     a.sort() 
#     i=0
#     j=1
#     o=n-1
#     ans=0 
#     while k>0:
#         suum=a[i]+a[j] 
#         if suum<=a[o]:
#             i+=2
#             j+=2 
#         else:
#             o-=1 
#         k-=1 
#         if k==0:
#             ans=sum(a[i:o+1])
#     print(ans)
    
        
   