t=int(input())
res=""
for _ in range(t):
    n,x=map(int,input().split())
    a=set(map(int, input().split()))
    v=1 
    while True :
        if v in a:
            v+=1 
        elif x>0:
            v+=1 
            x-=1 
        else:
            break
    res+=str(v-1)+"\n"
print(res)

            