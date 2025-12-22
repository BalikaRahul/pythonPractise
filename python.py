def rahul(a,b):
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            a=[i]+1
        else:
            b=b.append(a[i])
a=[1,2,3,4,5]
b=[]
result =rahul(a,b)
print(result)