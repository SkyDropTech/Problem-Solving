n=int(input())
s=list(map(int,input().split()))

one=s.count(1)
two=s.count(2)
three=s.count(3)
four=s.count(4)

ans=four

ans+=three
one=max(0,one-three)

ans+=two//2
two%=2

if two:
    ans+=1
    one=max(0,one-2)

ans+=(one+3)//4

print(ans)