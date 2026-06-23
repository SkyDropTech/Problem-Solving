a,b=map(int,input().split())
ct=a

while True:
    x=a//b  
    ct+=x 
    r=a%b 
    a=x+r 
    if x==0:
        break 
print(ct) 