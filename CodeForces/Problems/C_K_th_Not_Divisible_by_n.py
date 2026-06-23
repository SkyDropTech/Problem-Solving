t=int(input())
res=""
for _ in range(t):
    n,k=map(int,input().split())
    ct=0 
    num=1
    while True:
        if num%n!=0:
            ct+=1  
        if ct==k:
            res+=f"{ct}\n" 
            break
        num+=1 
print(res)


#Here i was trying to solve this question without anyalsing the pattern 
#So i never thought aboyt this question doing it automatically 
# i was solving manually thiat is bad 