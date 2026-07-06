s = input()
s = s[1:-1]          
s = s.split(",")     

freq = {}

for i in s:
    if i not in freq:
        freq[i] = 1

print(len(freq))