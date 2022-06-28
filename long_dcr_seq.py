def LDS(L):
    n = len(L)
    m = 0
    ml = []
    for i in range(n-1):
        l = [L[i]]
        fst = L[i]
        for j in range(i+1,n):
            if L[j] < fst:
                fst = L[j]
                l.append(L[j])
        if len(l) > m:
            m = len(l)
            ml = l
        if m >= n-i-1:
            return ml

print(LDS([int(i) for i in input().split()]))