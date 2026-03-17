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
# def leetcode344(s):
#     left =0
#     right=len(s)-1
#     while left < right:
#         s[left],s[right]=s[right],s[left]
#         left+=1
#         right-=1
#     return s
# s=["h","e","l","l","o"]
# result = leetcode344(s)
# print(result)
# def sorting(arr):
#     for i in range(len(arr)):
#         arr[i]=arr[i]**2
#     if len(arr)>1:
#         mid=len(arr)//2
#         left = arr[:mid]
#         right=arr[mid:]
#         sorting(left)
#         sorting(right)
#         i=j=k=0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k]=left[i]
#                 i+=1
#             else:
#                 arr[k]=right[j]
#                 j+=1
#             k+=1
#         while i < len(left):
#             arr[k]=left[i]
#             i+=1
#             k+=1
#         while j< len(right):
#             arr[k]=right[j]
#             j+=1
#             k+=1
#     return arr
            
# arr=[1,-2,3,4,5]
# result =sorting(arr)
# print(result)
# def leetcode(arr,target):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==target:
#                 return i,j
#     return "not found "
def leetcode167(arr,target):
    left =0
    right=len(arr)-1
    while left<right:
        total = arr[left]+arr[right]
        if total ==target:
            return left+1,right+1
        elif total < target:
            left+=1
        else:
            right-=1
    return "not found"
arr=[2,3,4]
target=6
result = leetcode167(arr,target)
print(result)