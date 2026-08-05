# Task 1
while True:
    password =input("enter admin password to login:")
    if password == 'admin':
        print('your have logged in successfully')
        break
    else:
        print('incorrect password!')


# Task 2
# using for loop
for i in range(1,100):
    if i <=57:
        print(i)
        break
# using while loop
n=1
while n<=100:
    print(n)
    if n ==57:
        break
    n+=1



# Task 3
name = input('enter the string: ')
name.lower()
count=0
for i in name:
    if i in 'aeiou':
        count+=1
print(f'the vowels in the given string is {count}')

# Task 4
arr = [23,55,66,97,67]
largest =0
for i in range(len(arr)):
    if largest < arr[i]:
        largest=arr[i]
print(f'the largest number in the given list : {largest}')



#Task 4
rev= input('enter the your string')
s=list(rev)
l=0
r=len(s)-1
while l<=r:
    s[l],s[r]=s[r],s[l]
    l+=1
    r-=1
print(s)