# t=int(input())
# res=""
# for _ in range(t):
#     x,y=map(int,input().split()) 
#     a,b=map(int,input().split()) 
#     lst=[] 
#     if y>=x:
#         as1=x*a+y*a
#         as2=((y-x)*a)+x*b 
#         lst.append(as1)
#         lst.append(as2)
#         q=min(lst)
#     else:
#         as1=x*a+y*a
#         as2=((x-y)*a)+y*b 
#         lst.append(as1)
#         lst.append(as2)
#         q=min(lst)
#     res+=str(q)+"\n"
# print(res)

# t=int(input())
# res=""
# for _ in range(t):
#     x,y=map(int,input().split()) 
#     a,b=map(int,input().split()) 
#     m=min(x,y) 
#     sol1=m*b+abs(x-y)*a 
#     sol2=(x+y)*a 
#     res+=str(min(sol1,sol2))+"\n"
# print(res)

t=int(input())
res=""
for _ in range(t):
    x,y=map(int,input().split()) 
    a,b=map(int,input().split()) 
    if b>=2*a: 
        sol=(x+y)*a
    else:
        sol=min(x,y)*b+abs(x-y)*a 
    res+=str(sol)+"\n"
print(res)