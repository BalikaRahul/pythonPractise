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
# print(result)
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        original = x
        rev =0
        while x>0:
            digit =x%10
            rev =rev*10+digit
            x=x//10
        if original ==x :
            return True
        return False
x =int(input("enter the number:"))
obj =Solution()
result = obj.isPalindrome(x)
print(result)
        