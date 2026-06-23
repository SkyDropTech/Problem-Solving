x=input() 
res=""
i=0
while i<len(x):
    digit=int(x[i])
    a=9-digit 

    if i==0 and digit==9:
        res+=x[i] 
    elif a<digit:
        res+=str(a) 
    else:
        res+=x[i]
    i+=1 
print(res)