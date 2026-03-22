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
# def leetcode167(arr,target):
#     left =0
#     right=len(arr)-1
#     while left<right:
#         total= arr[left]+arr[right]
#         if total == target:
#             return left+1,right+1
#         elif total < target:
#             left+=1
#         else:
#             right-=1
#     return "not found"
# arr=[2,3,4]
# target=6
# result = leetcode167(arr,target)
# print(result)
# def leetcode11(arr):
#     left =0
#     right =len(arr)-1
#     maximum=0
#     while left < right :
#         current =min(arr[left],arr[right])*(right-left)
#         if current > maximum:
#             maximum=current
#         elif arr[left]< arr[right]:
#             left+=1
#         else:
#             right-=1
#     return maximum
# arr=[2,3,4]
# result = leetcode11(arr)
# print(result)   
# def leetcode125(s):
#     i = ""
#     for char in s:
#         if char.isalnum():
#             i += char.lower() 
#     j=0
#     k=len(i)-1
#     while j<k:
#         if i[j]!=i[k]:
#             return False
#         elif i[j]==i[k]:
#             j+=1
#             k-=1
#     return True
# def leetcode80(arr):
#     left =2
#     right =2
#     while left < len(arr):
#         if arr[left]!=arr[right-2]:
#             arr[right]=arr[left]
#             right+=1 
#         left+=1
#     return right        
# arr=[0,0,1,1,1,1,2,3,3]
# result = leetcode80(arr)
# print(result)
# print(arr[:result])
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         result =[]
#         if len(nums)<3:
#             return result
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     if nums[i]+nums[j]+nums[k]==0:
#                         triplet = sorted([nums[i],nums[j],nums[k]])
#                         if triplet not in result:
#                             result.append(triplet)
#         return result
                            
# nums=[-1,0,1,2,-1,-4]
# sol=Solution()
# result =sol.threeSum(nums)
# print(result)
# def max_subarray_sum(arr, k):
#     window_sum = 0
#     max_sum = 0

#     # Step 1: first window
#     for i in range(k):
#         window_sum += arr[i]

#     max_sum = window_sum

#     # Step 2: slide the window
#     for i in range(k, len(arr)):
#         window_sum = window_sum - arr[i - k] + arr[i]
#         max_sum = max(max_sum, window_sum)

#     return max_sum


# # Example usage
# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# def onces(nums):
#     count =0
#     left =0
#     right=0
#     while right<len(nums):
#         if nums[left]==nums[right]:
#             left+=1
#             right+=1
#         elif nums[left]!=nums[right]:
#             count +=1
# def leetcode136(nums):
#     n=len(nums)
#     for i in range(n):
#         count=0
#         for j in range(n):
#             if nums[i]==nums[j]:
#                 count+=1
#         if count==1:
#             return nums[i]
#     return -1
# nums=[4,1,2,1,2]
# result=leetcode136(nums)
# print(result)
def leetcode136(nums):
    feq={}
    for num in nums:
        feq[num]=feq.get(num,0)+1
    for num in nums:
        if feq[num]==1:
            return num
    return -1
nums=[4,1,2,1,2]
result=leetcode136(nums)
print(result)