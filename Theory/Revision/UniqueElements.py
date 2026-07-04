arr=[1,5,6,2,9,2,4,7,1,3,6,4]
freq={} 
for i in arr:
    freq[i]=freq.get(i,0)+1 
for j in freq:
    if freq[j]>1:
        print(j)