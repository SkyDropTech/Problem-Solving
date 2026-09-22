n=[0,1,1,2,3,5,8,13,21,34]  
def recursion(n):
    if n==0 or n==1:
        return n 
    return recursion(n-1)+recursion(n-2) 
print(recursion(9))