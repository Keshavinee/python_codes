t=int(input())
for i in range(t):
    val=[int(x) for x in input().split()][:2]
    l=val[0]
    r=val[1]
    sum=0
    for j in range(l,r+1):
        a=str(j)
        count=0
        for m in range(len(a)):
            if (m+1)%2==0:
                if int(a[m])%2==0:
                    count+=1
            else:
                if int(a[m])%2!=0:
                    count+=1
        if count==len(a):
            sum+=1
    print("Case #{}:".format(i+1),sum)
            
