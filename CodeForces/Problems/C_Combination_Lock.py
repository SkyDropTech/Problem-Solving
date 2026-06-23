# t=int(input())

# for _ in range(t):
#     n=int(input())
#     lst1=[] 
#     lst2=[] 
#     if n%2==0:
#         print(-1) 
         
#     else:
#         for i in range(1,n+1):
#             if i%2!=0:
#                 lst1.append(i) 
#             else:
#                 lst2.append(i) 
#         lst=lst1+lst2 
#         print(*lst)
# print()

t=int(input())

for _ in range(t):
    lst=[] 
    n=int(input())
    if n%2==0:
        print(-1) 
      
    else:
        for i in range(1,n+1):
            val=(2*i)%n 
            if val == 0:
                val=n 
            lst.append(val) 
        print(*lst)
print()
