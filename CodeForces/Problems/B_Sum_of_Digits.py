n=input() 
ct=0 
while len(n)>1:
    suum=0
    for i in n:
        suum+=int(i) 
    n=str(suum) 
    ct+=1 
print(ct)