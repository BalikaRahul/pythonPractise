def lef(arr):
    k=[]
    for i in range(1,len(arr)):
        k.append(arr[i])
    k.append(arr[0])
    return k
arr = [2,3,4,5,6,7,8]
result=lef(arr)
print(result)
