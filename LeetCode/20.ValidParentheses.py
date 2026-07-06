s=input()
ct1=0
ct2=0
ct3=0 
ok=False
for i in s:
    if i=="[":
        ct1+=1
    elif i=="]":
        ct1-=1
    elif i=="{":
        ct2+=1
    elif i=="}":
        ct2-=1
    elif i=="(":
        ct3+=1
    else:
        ct3-=1
    
    if ct1==ct2==ct3==0:
        ok=True
    elif ct1=0 and ()

