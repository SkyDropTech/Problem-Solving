n=int(input())
if n>=0:
    print(n)
else:
    x=str(n) 
    rem1=x[:-1]
    rem2=x[:-2]+x[-1] 
    print(max(int(rem1),int(rem2)))
