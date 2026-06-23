#Good question. I was so close to think about this logic. 
# I didnt strick the logic of loop will be the 
# best for this question


n,m=map(int,input().split())
step=(n+1)//2 
for i in range(step,n+1):
    if i%m==0:
        print(i)
        break 
else:
    print(-1)
