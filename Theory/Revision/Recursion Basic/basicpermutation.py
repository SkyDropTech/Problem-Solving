def permutation(n): 
    if n==0 or n==1:
        return 1 
    return permutation(n-1)*n 
print(permutation(3))