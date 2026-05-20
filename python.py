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
# def leetcode136(nums):
#     feq={}
#     for num in nums:
#         feq[num]=feq.get(num,0)+1
#     for num in nums:
#         if feq[num]==1:
#             return num
#     return -1
# nums=[4,1,2,1,2]
# result=leetcode136(nums)
# print(result)
# def subArray(arr,k):
#     left =0
#     max_len=0
#     sum=0
#     count =0
#     for right in range(len(arr)):
#         while sum == k:
#             sum+=arr[right]
#             left+=1
#             count+=1
#         max_len=max(max_len,count)
#     return max_len
# arr=[10,5,2,7,1,9]
# k=15
# result =subArray(arr,k)
# print(result)
# def leetcode169(nums):
#     c={}
#     for i in nums:
#         if i not in c:
#             c[i]=1
#         else:
#             c[i]+=1
#     max_key = max(c, key=c.get)
#     return max_key, c[max_key]

# nums=[7,0,0,1,7,7,2,7,7]
# result= leetcode169(nums)
# print(result)
# def leetcode53(nums):
#     cur=0
#     max_sum=nums[0]
#     for i in range(len(nums)):
#         cur+=nums[i]
#         max_sum=max(cur,max_sum)
#         if cur < 0:
#             cur=0
#     return max_sum
# nums =[-2,1,-3,4,-1,2,1,-5,4]
# result = leetcode53(nums)
# print(result)
# def leetcode121(nums):
#     left =0
#     right=1
#     curr=0
#     max_sum=0
#     while right < len(nums):
#         if nums[left]<nums[right]:
#             curr=nums[right]-nums[left]
#             max_sum=max(curr,max_sum)
#         else:
#             left=right
#         right+=1
#     return max_sum
# nums=[7,1,5,3,6,4]
# result = leetcode121(nums)
# print(result)
# def leetcode2149(nums):
#     i=0
#     j=1
#     while j< len(nums):
#         if i%2==0 and nums[i]<0:
#             nums[i],nums[j]=nums[j],nums[i]
#         else:
#             i+=2
#             j+=2
#     return nums
# nums =[3,1,-2,-5,2,-4]
# result=leetcode2149(nums)
# print(result)
# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         count =0
#         n=len(nums)
#         for i in range(n):
#             if nums[i]>nums[(i+1)%n]:
#                 count+=1
#         return count<=1
# def leetcode2149(nums):
#     a=[]
#     b=[]
#     for n in nums:
#         if n>0:
#             a.append(n)
#         else:
#             b.append(n)
#     result=[]
#     for i in range(len(a)):
#         result.append(a[i])
#         result.append(b[i])
#     return result

# def leetcode35(self, nums, target):
#     if len(nums)>1:
#         low = 0 
#         high =len(nums)-1
#         while low <=high:
#             mid = (low+high)//2
#             if nums[mid]==target or nums[mid]> target :
#                 return mid
#             elif nums[mid]<target:
#                 low =mid+1
#             else:
#                 high=mid-1
#     return low
# nums=[1,3,5,6]
# target = 5
# result =leetcode35(nums,target)
# print(result)
# def leetcode1480(nums):
#     for i in rangex(1,len(nums)):
#         nums[i]+=nums[i-1]
#     return nums
# nums=[1,2,3,4]
# result = leetcode1480(nums)
# print(result)
# def leetcode167(nums,target):
#     l=0
#     r=len(nums)-1
#     s=0
#     while l<r:
#         s=nums[l]+nums[r]
#         if s==target:
#             return l+1,r+1
#         elif s<target:
#             l+=1
#         else:
#             r-=1
#     return "not Found"
# nums=[2,7,11,15]
# target=9
# result =leetcode167(nums,target)
# print(result)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l=0
#         r=len(s)-1
#         while l<r:
#             while l < r and not s[l].isalnum():
#                 l += 1
#             while l < r and not s[r].isalnum():
#                 r -= 1
#             if s[l].lower()!=s[r].lower():
#                 return "false"
#             l+=1
#             r-=1
#         return "true"
# def leetcode704(nums,target):
#     low =0
#     high=len(nums)-1
#     while low <= high:
#         mid=(low+high)//2
#         if nums[mid]==target:
#             return mid
#         elif nums[mid]<target:
#             low =mid+1
#         else:
#             high=mid-1
#     return -1
# nums = [-1,0,3,5,9,12]
# target = 9
# result=leetcode704(nums,target)
# print(result)
# class Solution:
#     def secondLargestElement(self, nums):
#         if len(nums)<2:
#             return None
#         l=float('-inf')
#         s=float('-inf')
#         for i in range(len(nums)):
#             if nums[i]>l:
#                 s=l
#                 l=nums[i]
#             elif l >nums[i]>s:
#                 s=nums[i]
#         if s==float('-inf'):
#             return -1
#         return s
# nums=[8, 8, 7, 6, 5]
# sol=Solution()
# result=sol.secondLargestElement(nums)
# print(result)
# def sorting(nums):
#     if len(nums)<1:
#         return None
#     if len(nums)>1:
#         mid = len(nums)//2
#         left=nums[:mid]
#         right=nums[mid:]
#         sorting(left)
#         sorting(right)
#         i=j=k=0
#         while i<len(left) and j< len(right):
#             if left[i]<right[j]:
#                 nums[k]=left[i]
#                 i+=1
#             else:
#                 nums[k]=right[j]
#                 j+=1
#             k+=1
#         while i <len(left):
#             nums[k]=left[i]
#             i+=1
#             k+=1
#         while j<len(right):
#             nums[k]=right[j]
#             j+=1
#             k+=1
#         return nums  
# nums=[8, 8, 7, 6, 5]
# result=sorting(nums)
# print(result)
# def searching(nums,target):
#     if len(nums)==1:
#         return nums
#     if len(nums)>2:
#         left=0
#         right=len(nums)-1
#         while left <= right:
#             mid =(left+right)//2
#             if nums[mid]==target:
#                 return mid+1
#             elif nums[mid]<target:
#                 left=mid+1
#             else:
#                 right=mid-1
#     return -1
# nums=[2,3,4,5,6,7,8,9]
# target=9
# result=searching(nums,target)
# print(result)
# def allZero(nums):
#     left =0
#     for right in range(len(nums)):
#         if nums[right]!=0:
#             nums[left],nums[right]=nums[right],nums[left]
#             left+=1
#     return nums
# nums=[1,2,0,2,0,3,0,9,0]
# result = allZero(nums)
# print(result)

# def leetcode9(self, x: int) -> bool:
#     s=str(x)
#     return s ==s[::-1]
# x=123
# result =leetcode9
# print(result)
# def waterProblem(nums):
#     left =0
#     right=len(nums)-1
#     maxi=0
#     while left<right:
#         cur =min(nums[left],nums[right])*(right-left)
#         if cur>maxi:
#             maxi =cur
#         elif nums[left]<nums[right]:
#             left+=1
#         else:
#             right-=1
#     return maxi
# nums=[1,8,6,2,5,4,8,3,7]
# result=waterProblem(nums)
# print(result)
# def leetcode3(s):
#     left=0
#     res=0
#     seen=set()
#     for right in range(len(s)):
#         while s[right] in seen:
#             seen.remove(s[left])
#             left+=1
#         seen.add(s[right])
#         res=max(res,right-left+1)
#     return res
# s='abcabcbb'
# result =leetcode3(s)
# print(result)

# def leetcode209(target,nums) -> int:
#     left =0
#     res =0
#     min_len=float('inf')
#     for right in range(len(nums)):
#         res+=nums[right]
#         while res>=target:
#             min_len=min(min_len,right-left+1)
#             res-=nums[left]
#             left+=1
#     return 0 if min_len ==float('inf') else min_len
# def leetcode424(s,k):
#     left =0
#     count ={}
#     maxCount=0
#     res=0
#     for right in range(len(s)):
#         count[s[right]]=count.get(s[right],0)+1
#         maxCount = max(maxCount,count[s[right]])
#         while (right-left+1)-maxCount>k:
#             count[s[left]]-=1
#             left+=1
#         res =max(res,right-left+1)
#     return res

# def leetcode3(s):
#     left =0
#     count=0
#     result =set()
#     for right in range(len(s)):
#         while s[right] in result:
#             result.remove(s[left])
#             left+=1
#         result.add(s[right])
#         count=max(count,right-left+1)
#     return count 
# s='ababababab'
# result = leetcode3(s)
# print(result)
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         l=0
#         r=0
#         while r<len(nums):
#             if nums[r]!=0:
#                 nums[l],nums[r]=nums[r],nums[l]
#                 l+=1
#             r+=1
#         return nums
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         l=0
#         r=len(s)-1
#         while l<=r:
#             s[l],s[r]=s[r],s[l]
#             l+=1
#             r-=1
#         return s
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         l=0
#         r=1
#         while r<len(nums):
#             if nums[l]!=nums[r]:
#                 l+=1
#                 nums[l]=nums[r]
#             r+=1
#         return l+1
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         l=0
#         r=len(nums)-1
#         while l<=r:
#             if nums[l]!=val:
#                 l+=1
#             else:
#                 nums[l],nums[r]=nums[r],nums[l]
#                 r-=1
        # return l        
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         l=0
#         r=len(numbers)-1
#         sumi=0
#         while l<=r:
#             sumi =numbers[l]+ numbers[r]
#             if sumi ==target:
#                 return l+1,r+1
#             elif sumi < target:
#                 l+=1
#             elif sumi > target:
#                 r-=1
#             else:
#                 return -1

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         l=0
#         r=len(height)-1
#         m=0
#         while l<=r:
#             c=min(height[l],height[r])*(r-l)
#             if m<c:
#                 m=c
#             elif height[l]<height[r]:
#                 l+=1
#             else:
#                 r-=1
#         return m

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
# def leetcode1004(nums,k):
#     left =0
#     zero=0
#     length=0
#     for right in range(len(nums)):
#         if nums[right]==0:
#             zero+=1
#         while zero>k:
#             if nums[left]==0:
#                 zero-=1
#             left+=1
#         length =max(length,right-left+1)
#     return length
# class Solution:
#     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
#         zeros=0
#         ones=0
#         sum =0
#         for i in range (len(students)):
#             if students[i]==0:
#                 zeros+=1
#             else:
#                 ones+=1
#         for j in range(len(sandwiches)):
#             if sandwiches[j]==0:
#                 if zeros==0:
#                     break
#                 zeros-=1
#             else:
#                 if ones==0:
#                     break
#                 ones-=1
#         sum =ones+zeros
#         return sum
# def leetcode42(nums):
#     l=0
#     r=len(nums)-1
#     lmax=0
#     rmax=0
#     total=0
#     while l<r:
#         if nums[l]<nums[r]:
#             if nums[l]>=lmax:
#                 lmax=nums[l]
#             else:
#                 total+=lmax-nums[l]
#             l+=1
#         else:
#             if nums[r]>=rmax:
#                 rmax=nums[r]
#             else:
#                 total+=rmax-nums[r]
#             r-=1
#         return total
# def binarySearch(arr,target):
#     if len(arr) <1:
#         return -1
#     if len(arr)>1:
#         l=0
#         r=len(arr)-1
#         ans = len(arr)
#         while l<=r:
#             mid= (l+r)//2
#             if arr[mid]>=target:
#                 ans =mid
#                 r=mid-1
#             else:
#                 l=mid+1
#         return ans
# arr=[0,1,2,3,3,4]
# target=3
# result= binarySearch(arr,target)
# print(result)
def LowerBoundbinarySearch(arr,target):
    if len(arr) <1:
        return -1
    if len(arr)>1:
        l=0
        r=len(arr)-1
        ans = len(arr)
        while l<=r:
            mid= (l+r)//2
            if arr[mid]>=target:
                ans =mid
                r=mid-1
            else:
                l=mid+1
        return ans
arr=[0,1,2,3,3,4]
target=3
result= LowerBoundbinarySearch(arr,target)
print(result)
        












    