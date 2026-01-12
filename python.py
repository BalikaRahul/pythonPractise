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
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
        