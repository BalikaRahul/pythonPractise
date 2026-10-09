# def reversecount(nums):
#     if nums==0:
#         return
#     print(nums)
#     return reversecount(nums-1)
# reversecount(4)


# def count(nums):
#     if nums ==0:
#         return nums
#     count(nums-1)
#     print(nums)
# count(4)

# def Sum(nums,total):
#     if nums ==0:
#         return total
#     total+=nums
#     return Sum(nums-1,total)
# print(Sum(4,0))


# def fact(nums):
#     if nums ==1:
#         return 1
#     return nums*fact(nums-1)
# print(fact(5))

# def power(base,exponent):
#     if exponent ==0:
#         return 1
#     return base*power(base,exponent-1)
#     ans=1
#     # for i in range(exponent):
#     #     ans*=base
#     # return ans
# print(power(4,5))




# def Sum(total,i,arr):
#     if i==len(arr):
#         return total
#     total+=arr[i]
#     return Sum(total,i+1,arr)
# total=0
# i=0
# arr=[10,20,30,40]
# print(Sum(total,i,arr))
    

# def reverse(s,i,rev):
#     if i==-1:
#         return rev
#     rev+=s[i]
#     return reverse(s,i-1,rev)
# s='PYTHON'
# i=len(s)-1
# rev=""
# print(reverse(s,i,rev))


# def largest(lar,arr,i):
#     if i ==len(arr):
#         return lar
#     lar=max(arr[i],lar)
#     return largest(lar,arr,i+1)
# i=0
# lar=float('-inf')
# arr=[10,455,23,78,12]
# print(largest(lar,arr,i))



# def even(n):
#     if n==0:
#         print(n)
#         return
#     even(n-1)
#     if n%2==0:
#         print(n)
# even(10)




# def totalSum(s,i,total):
#     if i==len(s):
#         return total
#     total+=int(s[i])
#     return (totalSum(s,i+1,total))
# i=0
# total=0
# s='1234'
# print(totalSum(s,i,total))


# def Palindrome(s,i,rev):
#     if i==-1:
#         if s==rev:
#             return "Palindrome"
#         else:
#             return "not palindrome"
#     rev+=s[i]
#     return Palindrome(s,i-1,rev)
# s='PYTHON'
# i=len(s)-1
# rev=""
# print(Palindrome(s,i,rev))


# def countVowels(s,i,total):
#     if i==len(s):
#         return total
#     if s[i] in 'aeiou':
#         total+=1
#     return (countVowels(s,i+1,total))
# i=0
# total=0
# s='Programming'
# print(countVowels(s,i,total))

def countUpper(s,i,total):
    if i==len(s):
        return total
    if s[i].isupper():
        total+=1
    return (countUpper(s,i+1,total))
i=0
total=0
s='PyTHon Is FuN'
print(countUpper(s,i,total))
