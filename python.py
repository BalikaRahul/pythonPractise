def missingNumber(a,m):
    sum =0
    for i in range(len(a)):
        sum+=a[i]
    n=m*(m+1)//2
    miss=n-sum
    return miss
a=[1,2,3,4,5,7]
m=len(a)+1
result = missingNumber(a,m)
print(result)