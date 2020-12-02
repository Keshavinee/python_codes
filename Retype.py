t=int(input())
for i in range(t):
    val=[int(x) for x in input().split()][:3]
    n=val[0]
    k=val[1]
    s=val[2]
    sum1=k-1+n
    sum2=2*k-2*s+n
    if sum1>=sum2:
        print("Case #{}:".format(i+1),sum2)
    else:
        print("Case #{}:".format(i+1),sum1)
    
