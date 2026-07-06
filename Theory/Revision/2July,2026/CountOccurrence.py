arr=[1,1,2,2,3,3,3,4,4,5,5,5,5,5,5,6,7]
#count how many time X number is appearing...
dict={} 
for i in arr:
    dict[i]=dict.get(i,0)+1
x=int(input())
print(dict.get(x))