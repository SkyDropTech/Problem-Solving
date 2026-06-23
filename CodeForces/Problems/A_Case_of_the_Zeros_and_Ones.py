def case_zero(n,s):
    x=s.count("1")
    y=s.count("0")
    return n-2*(min(x,y))

n=int(input())
s=input() 

print(case_zero(n,s))