t=int(input())
for i in range(t):
    n=int(input())
    f=[int(j) for j in input().split()][:n]
    a=f[0]
    dist=a
    while (a%n)!=0:
        if a>n:
            dist+=f[a-n]
        else:
            dist+=f[a-1]
        if a==dist%n:
            break
        a=dist%n    
    print(dist)    
        
