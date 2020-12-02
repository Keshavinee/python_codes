t=int(input())
for j in range(t):
    n=int(input())
    mnt=[int(k) for k in input().split()][:n]
    mnt.sort(reverse=True)
    count=mnt[0]
    sub=mnt[0]-mnt[1]
    for i in range(2,len(mnt),2):
        bur2=mnt[i]-sub
        if (i+1)<len(mnt):
            if mnt[i+1]>=mnt[i]:
                count+=mnt[i+1]
                sub=mnt[i+1]-bur2
            else:
                count+=bur2
                sub=bur2-mnt[i+1]
        else:
            count+=bur2
    print(count)        
            
    
    
            
    
 
           
    
