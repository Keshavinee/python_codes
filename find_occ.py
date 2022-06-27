def findOccOf(L,x):
    low = 0
    high = len(L)
    while (low <= high):
        mid = (low + high)//2
        if L[mid]==x:
            idx = mid
            while idx >= low and L[idx]==x:
                idx -= 1
            if (idx < low and L[idx+1] == x) or (idx >= low):
                a = idx + 1
            
            idx = mid
            while idx <= high and L[idx]==x:
                idx += 1
            if (idx > low and L[idx-1] == x) or (idx <= high):
                b = idx - 1
            
            return a,b

        elif x > L[mid]:
            low = mid + 1

        else:
            high = mid - 1
    return (None,None)        

A = [int(item) for item in input().split(" ")]
x = int(input())
timeout = 1.0 # Timeout in sec
