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
# def leetCode27(arr,target):
#     left =0
#     right =len(arr)-1
#     while left<right:
#         if arr[left]!=target:
#             left+=1
#         elif arr[left]==target:
#             arr[left],arr[right]=arr[right],arr[left]
#             right-=1
#     return left
# arr=[1,1,2]
# target=1
# result = leetCode27(arr,target)
# print(result)
# print(arr[:result])
# def leetCode283(arr):
#     left=0
#     right =0
#     while  right < len(arr):
#         if arr[right]!=0:
#             arr[left],arr[right]=arr[right],arr[left]
#             left+=1
#         right+=1
#     return arr
# arr=[0,1,0,0,1,2]
# result = leetCode283(arr)
# print(result)
def leetcode344(s):
    left =0
    right=len(s)-1
    while left < right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s
s=["h","e","l","l","o"]
result = leetcode344(s)
print(result)