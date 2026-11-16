t=int(input()) 
for _ in range(t):
    n=int(input()) 
    lst=[]
    if n<4:
        print(-1) 
    else:
        i=n
        while i>0:
            lst.append(i)
            i-=1
        
        if n%2==0:
            print(*lst) 
        else:
            lst[0],lst[1]=lst[1],lst[0] 
            lst[-2],lst[-1]=lst[-1],lst[-2]
            print(*lst)
    

