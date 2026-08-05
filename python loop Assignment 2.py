# easy
# Task 1
for i in range(1,100):
    if i%5==0:
        print(i)


#Task 2
n=int(input('enter the number: '))
Total=n*(n+1)//2
print(f'The sum of the first {n} number: {Total}')


#Task 3 
count=0
for i in range(1,100):
    if i%3==0:
        count+=1
print(f'The number that divisble by 3 between 1 to 100: {count}')



#Task4 
name = input('enter the your name: ')
for i in range(len(name)):
    print(name[i])


#Task 5
for i in range(1,100):
    if i%4==0:
        continue
    else:
        print(i)

# medium Task
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

# challenges
# Task 1
n =int(input('enter the number: '))
is_prime =True
for i in range(2,n):
    if n%i==0:
        is_prime = False
        break
if is_prime:
    print("not a prime number")
else:
    print('it is a prime number')



    
# Task 2 using recursion
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input('enter the number: '))
result = fib(n)
print(result)




# Task 4
while True:
    num = int(input('enter the number: '))
    if num == 3:
        print(f'you have guessed the number :{num}')
        break
    elif num >3:
        print('the number is lower than your guess  ')
    elif num< 3:
        print('the number is higher than your guess ')
    else:
        print('wrong guess')








