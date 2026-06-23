t=int(input())
res=""
for _ in range(t):
    a,b,c,d=map(int,input().split())
    if b>a:
        if (a<c<b and (b<d or d<a)) or (a<d<b and (b<c or c<a)):
            res+="YES\n"
        else:
            res+="NO\n"
    else:
        if (b<c<a and (a<d or d<b)) or (b<d<a and (a<c or c<b)):
            res+="YES\n"
        else:
            res+="NO\n"

print(res)

#########2nd methd to solve the same question#######
# t=int(input())
# res=""

# for _ in range(t):
#     a,b,c,d=map(int,input().split())
    
#     x=a
#     f1=False
#     f2=False
    
#     while x!=b:
#         x=x%12+1
#         if x==c:
#             f1=True
#         if x==d:
#             f2=True
    
#     if f1!=f2:
#         res+="YES\n"
#     else:
#         res+="NO\n"

# print(res)
