pos=input().upper()
text=input()
result=""
keyboard  = [
    ['q','w','e','r','t','y','u','i','o','p'],
    ['a','s','d','f','g','h','j','k','l',';'],
    ['z','x','c','v','b','n','m',',','.','/']
]
for ch in text:
    for i in range(len(keyboard)):
        for j in range(len(keyboard [i])):
            if keyboard[i][j]==ch:
                if pos=="R":
                    result+=keyboard[i][j-1]
                else:
                    result+=keyboard[i][j+1]
print(result)
