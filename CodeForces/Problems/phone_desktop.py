t=int(input())
res=""
for _ in range(t):
    x,y=map(int,input().split())
    screen=y//2 
    if y%2==1:
        screen+=1 
        x-=11 
    x-=(y//2)*7 
    if x>0:
        screen+=(x+14)//15 
    res+=str(max(screen,0))+"\n"
print(res)
