s=input()
if len(s)==1:
    if s.islower():
        print(s.upper())
    else:
        print(s.lower())
elif (s[0].islower() and s[1:].isupper()):
    x=s[0].upper()
    y=s[1:].lower()
    print(f"{x}{y}")
elif s.isupper():
    x=s[0].lower()
    y=s[1:].lower()
    print(f"{x}{y}")
else:
    print(s)
