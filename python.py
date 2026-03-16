def leetCode26(arr):
    left =0
    right =1
    while right<len(arr):
        if arr[left]!=arr[right]:
            left+=1
            arr[left]=arr[right]
        right+=1
    return left+1
arr=[1,1,2]
result = leetCode26(arr)
print(result)
print(arr[:result])