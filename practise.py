# def twoSum2(arr,target):
#     l=0
#     r=len(arr)-1
#     while l<r:
#         Sum=arr[l]+arr[r]
#         if Sum==target:
#             return [l+1,r+1]
#         elif Sum<target:
#             l+=1
#         else:
#             r-=1
#     return -1
# arr=[2,7,11,15]
# target = 9
# print(twoSum2(arr,target))

# def moveZeroes( nums) :
#     l=0
#     r=1
#     while r<len(nums):
#         if nums[r]!=0:
#             nums[l],nums[r]=nums[r],nums[l]
#             l+=1
#         r+=1
#     return nums
# nums=[0,1,0,1,0,0,2]
# print(moveZeroes(nums))




# def threeSum(arr, target):
#     res = []

#     if not arr or len(arr) < 3:
#         return res

#     arr.sort()

#     for i in range(len(arr) - 2):

#         # Skip duplicates
#         if i > 0 and arr[i] == arr[i - 1]:
#             continue

#         l, r = i + 1, len(arr) - 1

#         while l < r:
#             total = arr[i] + arr[l] + arr[r]

#             if total == target:
#                 res.append([arr[i], arr[l], arr[r]])

#                 # Skip duplicate left values
#                 while l < r and arr[l] == arr[l + 1]:
#                     l += 1

#                 # Skip duplicate right values
#                 while l < r and arr[r] == arr[r - 1]:
#                     r -= 1

#                 l += 1
#                 r -= 1

#             elif total < target:
#                 l += 1

#             else:
#                 r -= 1

#     return res


# arr = [-1, 1, 5, 5, 7]
# target = 6

# print(threeSum(arr, target))
# def maxArea(nums):
#     l=0
#     r=len(nums)-1
#     maxi=float('-inf')
#     while l<r:
#         current = min(nums[l],nums[r])*(r-l)
#         maxi =max(current,maxi)
#         if nums[l]<nums[r]:
#             l+=1 
#         else:
#             r-=1
#     return maxi
# def Sort(nums):
#     if len(nums)<=1:
#         return nums
#     mid=len(nums)//2
#     left=nums[:mid]
#     right=nums[mid:]
#     Sort(left)
#     Sort(right)
#     i=j=k=0
#     while i<len(left) and  j <len(right):
#         if left[i]<right[j]:
#             nums[k]=left[i]
#             i+=1
#         else:
#             nums[k]=right[j]
#             j+=1
#         k+=1
#     while i<len(left):
#         nums[k]=left[i]
#         i+=1
#         k+=1
#     while j<len(right):
#         j+=1
#         k+=1
#     return nums
# nums=[0,2,3,1,5,8,9]
# print(Sort(nums))
# def waterProblem(nums):
#     total=0
#     l=0
#     lmax=float('-inf')
#     r=len(nums)-1
#     rmax=float('-inf')
#     while l<r:
#         current =min(lmax,rmax)
#         if lmax<=rmax:
#             lmax=max(nums[l],lmax)
#             total+=lmax-nums[l]
#             l+=1
#         else:
#             rmax=max(nums[r],rmax)
#             total+=rmax-nums[r]
#             r-=1
#     return total
# nums=[0,1,0,2,1,0,1,3,2,1,2,1]
# print(waterProblem(nums))
# class Solution:
#     def trap(self, height: list[int]) -> int:
#         total =0
#         l=0
#         lmax=float('-inf')
#         r=len(height)-1
#         rmax =float('-inf')
#         while l<r:
#             if height[l]<height[r]:
#                 lmax = max(height[l],lmax)
#                 total+=lmax-height[l]
#                 l+=1
#             else:
#                 rmax=max(height[r],rmax)
#                 total+=rmax-height[r]
#                 r-=1
#         return total
# a=[1,2,3]
# print(a*2)
# print([i for i in range(5) if i % 2 == 0])
# x = [1, 2, 3]
# print(x.pop(), x)
# arr=[1,3,-1,5,3,6,7]
# l=0
# k=3
# nums=[]
# maxi=0
# for i in range(k,len(arr)):
#     maxi=max(arr[i])
#     nums.append(maxi)
#     l+=1
# print(nums)

# def prefixBasic(nums):
#     n=len(nums)
#     p=[0]*n
#     p[0]=nums[0]
#     for i in range(1,len(nums)):
#         p[i]=(p[i-1]+nums[i])
#     return p
# nums=[10,20,30,40,50,60]
# print(prefixBasic(nums))\
# def subarraySum(nums, k ):
#     Sum =0
#     maxlen=0
#     p={0:1}
#     for r in range(len(nums)):
#         Sum+=nums[r]
#         diff =Sum-k
#         if diff in p:
#             maxlen+=p[diff]
#             print(p[diff])
#         p[Sum] = p.get(Sum, 0) + 1
#     return maxlen
# nums=[1,2,3]
# k=3
# print(subarraySum(nums,k))
def subarraysWithKDistinct(nums,k):
    d={}
    l=0
    count=0
    for i in range(len(nums)):
        d[nums[i]] = d.get(nums[i], 0) + 1
        while len(d)>k:
            d[nums[l]]-=1
            if d[nums[l]]==0:
                del d[nums[l]]
            l+=1
        count+=i-l+1
    return count 
nums = [1,2,1,2,3]
k = 2
print(subarraysWithKDistinct(nums,k))

def subarraysWithKDistinct(nums, k):

    def atMost(k):
        d = {}
        l = 0
        count = 0

        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1

            while len(d) > k:
                d[nums[l]] -= 1

                if d[nums[l]] == 0:
                    del d[nums[l]]

                l += 1

            count += i - l + 1

        return count

    return atMost(k) - atMost(k - 1)


nums = [1, 2, 1, 2, 3]
k = 2

print(subarraysWithKDistinct(nums, k))
