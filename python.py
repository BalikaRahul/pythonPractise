# def leetCode26(arr):
#     left =0
#     right =1
#     while right<len(arr):
#         if arr[left]!=arr[right]:
#             left+=1
#             arr[left]=arr[right]
#         right+=1
#     return left+1
# arr=[1,1,2]
# result = leetCode26(arr)
# print(result)
# print(arr[:result])
def leetCode27(arr,target):
    left =0
    right =len(arr)-1
    while left<right:
        if arr[left]!=target:
            left+=1
        elif arr[left]==target:
            arr[left],arr[right]=arr[right],arr[left]
            right-=1
    return left
arr=[1,1,2]
target=1
result = leetCode27(arr,target)
print(result)
print(arr[:result])
    
