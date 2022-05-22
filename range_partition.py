z = 0
def printAllSubsetsRec(arr, n, v, sum) :
    global z
    if (sum == 0) :
        if z==0:
            print(len(v))
            for value in v :
                print(value, end=" ")
            print()
            z+=1
        return

    if (n == 0):
        return
 
    printAllSubsetsRec(arr, n - 1, v, sum)
    v1 = [] + v
    v1.append(arr[n - 1])
    printAllSubsetsRec(arr, n - 1, v1, sum - arr[n - 1])
 
 
    
t = int(input())

for j in range(t):
    n, x, y = [int(i) for i in input().split()]
    l=[];v=[]

    sum = 0
    for i in range(1,n+1):
        sum+=i
        l.append(i)
    
    nmt = (x*sum)/(x+y)
    nmt1 = (x*sum)//(x+y)
    dmt = sum - nmt

    if nmt==nmt1:
        print("Case #{}: {}".format(j+1,"POSSIBLE"))
        printAllSubsetsRec(l, n, v, nmt1)
        z = 0
    else:
        print("Case #{}: {}".format(j+1,"IMPOSSIBLE"))