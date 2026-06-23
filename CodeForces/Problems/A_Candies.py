# (1 << (i + 1)) - 1 This is some new concept 
# we will learn about this later 

t=int(input())
res=""
for _ in range(t):
    n=int(input())
    suum=1
    i=1 
    while True:
        suum+=2**i 
        if n%suum==0:
            res+=f"{n//suum}\n"
            break 
        i+=1 
print(res) 




