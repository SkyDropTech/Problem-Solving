n=int(input())
names=["Sheldon", "Leonard","Penny","Rajesh","Howard"]
k=1 
while n>5*k:
    n-=5*k 
    k*=2 
i=(n-1)//k 
print(names[i])