t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split()) 
    x=abs(a-b) 
    y=abs(b-c) 
    z=abs(c-a) 
    print(min(x,y,z))