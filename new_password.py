t = int(input())

for i in range(t):
    n = int(input())
    pwd = input()
    
    l=u=d=s=0
    for c in pwd:
        if c.islower():
            l+=1
        elif c.isupper():
            u+=1
        elif c.isdigit():
            d+=1
        elif c in "#@*&":
            s+=1
    
    if l==0:
        pwd+='a'
    if u==0:
        pwd+='A'
    if d==0:
        pwd+='1'
    if s==0:
        pwd+='&'   
    if len(pwd)<7:
        for i in range(7-len(pwd)):
            pwd+='#'

    print("Case #{}: {}".format(i+1,pwd))