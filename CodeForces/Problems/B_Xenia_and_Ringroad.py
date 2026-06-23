n,m=map(int, input().split())
a=list(map(int, input().split()))
time=0
pos=1
for house in a:
    if house>=pos:
        time+=house-pos
    else:
        time+=(n-pos)+house
    pos=house

print(time)