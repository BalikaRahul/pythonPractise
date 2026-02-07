# def Reverse(num):
#     rev =0
#     while num >0:
#         digit =num%10
#         rev = rev*10+digit
#         num //=10
#     return rev
# num=int(input("enter a number"))
# result=Reverse(num)
# print(result)
# def MoveZeroToEnd(num):
#     for i in range(len(num)):
#         for j in range(len(num)-1):
#             if(num[j]==0 or num[j+1]!=0):
#                 num[j],num[j+1]=num[j+1],num[j]
#     return num
# num=[1,0,1,0,1,0]
# result = MoveZeroToEnd(num)
# print(num)
# def TargetSum(num,Target):
#     for i in range(len(num)):
#         demo=num[i]-Target
#         if(demo ==num[i-1]):
#             return "yes"
# num =[1,2,3,4,5,6]
# Target = int(input('enter the number'))
# result = TargetSum(num,Target)
# # print(result)
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         original = x
#         rev =0
#         while x>0:
#             digit =x%10
#             rev =rev*10+digit
#             x=x//10
#         if original ==x :
#             return True
#         return False
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x < 0:
#             return False

#         original = x   # ✅ STORE ORIGINAL VALUE
#         rev = 0

#         while x > 0:
#             digit = x % 10
#             rev = rev * 10 + digit
#             x //= 10

#         return original == rev
# class Solution:
#     def printNumber(self,n):
#         return n
# n=int(input("enter the number"))
# obj=Solution()
# result = obj.printNumber(n)
# print(result)
# class Solution:
#     def studentGrade(self, marks):
#         if(marks >=90):
#             return "A"
#         elif(marks >=70):
#             return "B"
#         elif(marks  >=50):
#             return "C"
#         elif(marks >=35):
#             return "D"
#         else :
#             return "Fail"
# marks=int(input("enter the marks: "))
# obj=Solution()
# result =obj.studentGrade(marks)
# print(result)
# class Solution:
#     def whichWeekDay(self, day):
#         match day:
#             case 1:
#                 return("sunday")
#             case 2:
#                 return("monday")
#             case 3:
#                 return("Tuesday")
#             case 4:
#                 return("Wednesday")
#             case 5:
#                 return("Thursday")
#             case 6:
#                 return("Friday")
#             case 7:
#                 return("Saturday")
#             case _:
#                 return("invalid input")

# day = int(input("enter the number between 1 to 7: "))
# obj=Solution()
# result=obj.whichWeekDay(day)
# print(result)
# n=5
# for i in range(n):
#     print(" "*(n-i-1),end="")
#     print("*"*(2*i-1),end="")
#     print(" "*(n-i-1))

# for i in range(n):
#     print(" "*i,end="")
#     print("*"*(2*n-(2*i+1)),end="")
#     print(" "*i)
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     print()
# n=2345
# count =0
# while n>0:
#     n=n//10
#     count+=1
# print(count)
# def rev(n):
#     rev =0
#     while n > 0:
#         digit = n%10
#         rev =rev*10+digit
#         n//=10
#     return rev
# n = 2345
# result = rev(n)
# print(result)
# def Reverse(num):
#     rev =0
#     while num >0:
#         digit =num%10
#         rev = rev*10+digit
#         num //=10
#     return rev
# num=int(input("enter a number"))
# result=Reverse(num)
# print(result)
# def printAll(n,count):
#     for i in range(1,n+1):
#         if (n%i==0):
#             count +=1
#     if count <=2:
#         return ("it is prime number")
#     else:
#         return ("it is not a prime")
#     # return count
# n=int(input("enter the number: "))
# count =0
# result=printAll(n,count)
# print(result)
# def recursion(n):
#     return recursion
# n= "rahul"
# result = recursion(n)
# print(recursion)
# def printName(n):
#     fib=0
#     if n==0:
#         return 0   
#     return fib+printName(n-1)
    
    
# print(printName(5))
# def nothing(nums):
#     rev =0
#     while(nums>0):
#         digit = nums%10
#         rev = rev*10+ digit
#         nums//=10
#     return rev
# nums=987
# result =nothing(nums)
# print(result)
# def sort(arr):
#     for i in range(len(arr)-1):
#         for j in range( i+1,len(arr)):
#             if(arr[i]<arr[j]):
#                 arr[i],arr[j]=arr[j],arr[i]
#     return arr
# arr=[1,4,2,5,8]
# result =sort(arr)
# print(result)
# def sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-i-1):
#             if(arr[j]>arr[j+1]):
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# arr=[1,4,2,5,8]
# result =sort(arr)
# print(result)
# def sort(arr):
#     for i  in range(1,len(arr)):
#         key =arr[i]
#         j=i-1
#         while j>=0 and arr[j]>key:
#             arr[j+1]=arr[j]
#             j-=1
#             arr[j+1]=key 
#     return arr
# arr=[1,4,2,5,8]
# result =sort(arr)
# print(result)
# def SumOf(arr):
#     sum=0
#     for i in range(len(arr)):
#         sum+=arr[i]
#     return sum
# arr=[1,2,3,4,10,11]
# result =SumOf(arr)
# print(result)
# def staircase(n):
#     for i in range(1, n + 1):
#         print(" " * (n - i) + "#" * i)

# staircase(6)  

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

# def staircase(n):
#     # Write your code here
#     for i in range(1,n+1):
#         print(" "*(n-i)+"#"*i)

# staircase(6)

# if __name__ == '__main__':
#     n = int(input().strip())

#     staircase(n)
# def gradingStudents(grades):
#     for i in range(len(grades)):
#         if grades[i]>=38:
#             next=((grades[i]//5)+1)*5
#             if next -grades[i]<3:
#                 grades[i] = next 
#     return grades
# grades = [38,56,23,39,59]
# result =gradingStudents(grades)
# print(result)
# def divisibleSumPairs(n,ar):
#     k=[]
#     for i in range(len(ar)-1):
#         for j in range(i+1,len(ar)):
#             if (ar[i]+ar[j] )%n ==0:
#                 k.append((ar[i],ar[j]))
                
#     return k
# ar=[1,2,3,4,5,4,2,2]

# n=5
# result = divisibleSumPairs(n,ar)
# print(result)
# def largestElements(arr):
#     largest =0
#     for i in range(len(arr)):
#         if(arr[i]>largest ):
#             largest =arr[i]
#     return largest
# arr=[2,3,4,7,8,10,11]
# result =largestElements(arr)
# print(result)
# def secondLargest(arr):
#     second =0
#     largest =0
#     for i in range(len(arr)):
#         if(arr[i]>largest):
#             second=largest
#             largest =arr[i]
#     return largest,second
# arr=[2,3,4,7,8,10,11,12]
# result =secondLargest(arr)
# print(result)
# def SortedOrNot(arr):
#     for i in range(len(arr)-1):
#         if(arr[i]>arr[i+1]):
#             return "not sorted"
#     return " sorted"
# arr=[2,3,4,1,7,8,11,12,10]
# result =SortedOrNot(arr)
# print(result)
# def lef(arr):
#     k=[]
#     for i in range(1,len(arr)):
#         k.append(arr[i])
#     k.append(arr[0])
#     return k
# arr = [2,3,4,5,6,7,8]
# result=lef(arr)
# print(result)
# def RemoveDeplicates(arr):
#     k=[]
#     for i in arr:
#         if i not in k:
#             k.append(i)
#     return k
# arr=[2,3,3,4,1,7,8,11,2,12,10]
# result =RemoveDeplicates(arr)
# print(result)
# def leftByD(arr,n,direction):
#     k=[]
#     if (direction=="left"):
#         for i in range(n,len(arr)):
#             k.append(arr[i])
#         for j in range(0,n):
#             k.append(arr[j])
#     else:
#         for i in range(len(arr)-1,-n):
#             k.append(arr[i])
#         for j in range(0,len(arr)):
#             k.append(arr[j])
#     return k
# arr=[2,3,3,4,1,7,8,11,2,12,10]
# direction=input("enter left or right: ")
# n=3
# result =leftByD(arr,n,direction)
# print(result)
# def moveZero(arr):
#     j=0
#     for i in range(len(arr)):
#             if(arr[i]!=0):
#                 arr[j],arr[i]=arr[i],arr[j]
#                 j+=1
#     return arr
# arr=[1,0,0,1,1,0,0]
# result=moveZero(arr)
# print(result)
#just to maintain streak 
# def even(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# n=2
# result =even(n)
# print(result)
# def union(arr1,arr2):
#     k=[]
#     for i in arr1:
#         if i not in k:
#              k.append(i)
#         for j in arr2:
#             if j not in k:
#              k.append(j)
#     return k
# arr1=[1,2,3,4,5]
# arr2=[1,3,4,5,6]
# result =union(arr1,arr2)
# print(result)
# def missingNumber(arr):
#     sum =0
#     n=len(arr)+1
#     for i in range(len(arr)):
#         sum+=arr[i]
#     m =n*(n+1)/2
#     dif =m-sum
#     return dif
# arr=[1,3,4,5,6]
# result =missingNumber(arr)
# print(result)
# def maxi(arr):
#     maxim =0
#     count =0
#     for i in range(len(arr)):
#         if(arr[i]==1 ):
#             count +=1
#         else:
#             count =0
#         maxim = max(maxim,count)
#     return maxim
# arr=[1,1,1,0,1,1,0,0,1,0,1]
# result =maxi(arr)
# print(result)
# sql prep
# def CountOne(arr):
#     for i in range(len(arr)):
#         count =0
#         for j in range(len(arr)):
#             if arr[j]==arr[i]:
#                 count +=1
#         if count ==1:
#             return arr[i]
#     return -1
# arr=[2,2,5,3,4,4,3]
# result= CountOne(arr)
# print(result)
# def targetVal (arr,target):
#     maxLength=0
#     for i in range(len(arr)):
#         current =0
#         for j in range(i,len(arr)):
#             for k in range(i,j+1):
#                 current+=arr[k]
#             if current ==target :
#                 maxLength=max(maxLength,j-i+1)
#     return maxLength
# arr = [2,3,4,4,3,3,1,5,8]
# target =10
# result =targetVal(arr,target)
# print(result)
# def sort (arr):
#     if(len(arr)>1):
#         mid =len(arr)//2
#         left =arr[:mid]
#         right=arr[mid:]
#         sort(left)
#         sort(right)
#         i=j=k=0
#         while i<len(left) and j <len(right):
#             if left[i]<right[j]:
#                 arr[k]=left[i]
#                 i+=1
#             else:
#                 arr[k]=right[j]
#                 j+=1
#             k+=1
#         while i<len(left):
#             arr[k]=left[i]
#             i+=1
#             k+=k
#         while j <len(right):
#             arr[k]=right[j]
#             j+=1
#             k+=1
#     return arr
# arr = [2,4,1,5,6,8,9]
# result =sort(arr)
# print(arr)
# def search(arr,target):
#     n=len(arr)
#     low =0
#     high=n-1
#     while low <=high:
#         mid=(low+high)//2
#         if (arr[mid]==target):
#             return "found at index",mid+1
#         elif (target >arr[mid]):
#             low = mid+1
#         else:
#             high =mid-1
#     return -1
# arr= [1,2,3,4,5,6,7,23]
# target =23
# result = search(arr,target)
# print(result)
# # n=5
# for i in range(n+1):
#     for j in range(n,i,-1):
#         print("*",end=" ")
#     print( )
# arr=[1,3,4,5,6,7]
# for i in range(1,len(arr)):
#     if (arr[i]!=i):
#         print(i)
# def missingNumber(arr):
#     sum =0
#     n =len(arr)+1
#     for i in range(len(arr)):
#         sum+=arr[i]
#     n=n*(n+1)//2
#     dif =n - sum 
#     return dif
# arr=[1,3,4,5,6,7]
# result =missingNumber(arr)
# print(result)
# def AddingOfNumber(arr,target):
#     sum =0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if (target-arr[i]==arr[j]):
#                 sum =arr[j]
#     return sum
# arr=[1,3,4,5,6,7]
# target =int(input("enter the number:"))
# result =AddingOfNumber(arr,target)
# print(result)
# def search (arr,target):
#     low =0
#     high =len(arr)-1
#     while low <=high:
#         mid =(low+high)//2
#         if (arr[mid]==target):
#             return mid
#         elif arr[mid]<target:
#             low =mid+1
#         else :
#             high =mid-1
#     return -1
# arr= [1,2,3,4,5,6,7,23]
# target =23
# result = search(arr,target)
# print(result)
# class Solution:
#     def search(self, nums, target):
#         low =0
#         high =len(arr)-1
#         while low <= high:
#             mid = (low +high)//2
#             if (nums[mid]==target):
#                 return mid
#             elif nums[mid]<target:
#                 low =mid+1
#             else:
#                 high =mid-1
#         return -1
# arr =[1,2,3,4,5,6,8,9]
# target =9
# Sol=Solution()
# result =Sol.search(arr,target)
# print(result)
# def merge(arr):
#     if (len(arr)>1):
#         mid = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]
#         merge(left)
#         merge(right)
#         i=j=k=0
#         while i<len(left) and j <len(right):
#             if left[i] <right[j]:
#                 arr[k]=left[i]
#                 i+=1
#             else:
#                 arr[k]=right[j]
#                 j+=1
#             k+=1
#         while i<len(left):
#             arr[k]=left[i]
#             i+=1
#             k+=1
#         while j<len(right):
#             arr[k]=right[j]
#             j+=1
#             k+=1
#     return arr
# arr=[1,0,2,1,0]
# result =merge(arr)
# print(result)
# class Solution:
#     def sortZeroOneTwo(self, nums):
#         if (len(nums)>1):
#             mid = len(nums)//2
#             left = nums[:mid]
#             right = nums[mid:]
#             self.sortZeroOneTwo(left)
#             self.sortZeroOneTwo(right)
#             i=j=k=0
#             while i <len(left) and j <len(right):
#                 if (left[i]<right[j]):
#                     nums[k]=left[i]
#                     i+=1
#                 else:
#                     nums[k]= right[j]
#                     j+=1
#                 k+=1
#             while i<len(left):
#                 nums[k]=left[i]
#                 i+=1
#                 k+=1
#             while j<len(right):
#                 nums[k]=right[j]
#                 j+=1
#                 k+=1
#         return nums
# nums=[1,0,2,1,0]
# sol=Solution()
# result =sol.sortZeroOneTwo(nums)
# print(result)
# def searching(target,arr):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if (arr[i]+arr[j]==target):
#                 return i,j
#             return 0

# arr=[2,6,5,8,11]
# target =7
# result=searching(target,arr)
# print(result)
# def Search(target,arr):
#     seen =set()
#     for i in arr:
#         if (target-i in seen):
#             return target-i,i
#         seen.add(i)

# arr=[2,6,5,8,11]
# target =7
# result=Search(target,arr)
# print(result)
# def Sum(arr):
#     n=len(arr)
#     count =0
#     if (n<0):
#         return 0
#     else:
#         for i in range(n-1):
#             if (arr[i]==arr[i+1]):
#                 count+=1
#         return count,arr[i]
# def Sum(arr):
#     for i in range(len(arr)):
#         num =arr[i]
#         count =0
#         for j in range(len(arr)):
#             if arr[j]==num:
#                 count+=1
#             if count ==1:
#                 return num
#         return -1


# arr = [2,3,4,4,3,3,1,5,8]
# result =Sum(arr)
# print(result)
def movingAllZero(arr):
    n=len(arr)
    if(n<0):
        return 0
    left =0
    right = n-1
    while left < right:
        if arr[left] !=0 :
            left+=1
        elif arr[right] ==0:
            right-=1
        else:
            arr[left],arr[right]=arr[right],arr[left]
            left +=1
            right -=1
    return arr
arr = [1,0,1,0,0,0,1]
result =movingAllZero(arr)
print(result)