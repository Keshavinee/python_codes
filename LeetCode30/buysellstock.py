# Given price of stock for each day, write a program to compute maximum possible 
# profit by making multiple transactions.
# This is a good example of Dynamic Programming problem

# [7,1,5,3,6,4] max profit = 7 

def maxprofit(arr,n,p=0,m=[0],i=0,j=1):
    if j < n:
        if arr[i] < arr[j]:
            maxprofit(arr,n,p+(arr[j]-arr[i]),m,j+1,j+2)

        maxprofit(arr,n,p,m,i,j+1)

    else:
        if p > m[0]:
            m[0] = p
        
        while (i+1) < (n-1):
            maxprofit(arr,n,0,m,i+1,i+2)
            i += 1

def buysell(arr):
    m = [0]
    maxprofit(arr,len(arr),0,m)
    return m[0]

print("Maximum profit: ",buysell(eval(input())))
