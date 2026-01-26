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
def divisibleSumPairs(n,ar):
    k=[]
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            if (ar[i]+ar[j] )%n ==0:
                k.append((ar[i],ar[j]))
                
    return k
ar=[1,2,3,4,5,4,2,2]

n=5
result = divisibleSumPairs(n,ar)
print(result)