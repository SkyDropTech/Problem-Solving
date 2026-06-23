n=int(input())
w=list(map(int,input().split()))
suum=0 
i=0
while True:
    suum+=w[i]
    
    if suum>=n:
        print(i+1)
        break 
    
    i=(i+1)%len(w) 