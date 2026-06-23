p=input() 
x="HQ9"
ct=0
t=False
for i in p:
    for j in x:
        if i == j:
            ct+=1 
    if ct>0:
        t=True
if t:
    print("YES")
else:
    print("NO")