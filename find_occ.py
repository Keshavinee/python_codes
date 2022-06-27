def findOccOf(L,x):
    t=[]
    f=False
    for i in range(len(L)):
        if L[i]==x:
            if len(t)==0:
                t.append(i)
            f=True
        else:
            if f:
                return (t[0],i-1)
    return (None,None)
A = [int(item) for item in input().split(" ")]
x = int(input())
timeout = 1.0 # Timeout in sec