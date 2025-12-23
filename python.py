def leftRotate(arr):
    n=int(input("enter the number:"))
    k=n
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
        arr[-i]=arr[i]
    return arr

arr=[1,2,3,4,5]
result=leftRotate(arr)
print(result)