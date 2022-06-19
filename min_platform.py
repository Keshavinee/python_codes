def minimum_platform(l):
    d={0:[l[0]]}
    i = 0
    for j in range(1,len(l)):
        t = l[j]
        g = 0
        for k in d:
            f = 0
            for m in d[k]:
                if t[1]>=m[1] and t[1]<m[2]:
                    f = 1
                    break
            if f==0:
                d[k].append(t)
                g = 1
                break
        if g==0:
            i+=1
            d[i] = [t]
            
    return len(d)

schedule = eval(input())           
print(minimum_platform(schedule))