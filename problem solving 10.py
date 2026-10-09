# 1. Print Numbers from 1 to n
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(i, end=" ")


# 2. Print Numbers from m to n
m = int(input("Enter m value: "))
n = int(input("Enter n value: "))
for i in range(m, n+1):
    print(i, end=" ")


# 3. Print Numbers from n to 1 in Reverse
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i, end=" ")

# 4. Print Numbers from n to m in Reverse
n = int(input("Enter n value: "))
m = int(input("Enter m value: "))
for i in range(n, m-1, -1):
    print(i, end=" ")


# 5. Sum of n Natural Numbers
n = int(input("Enter a number: "))
s = 0
for i in range(n+1):
    s += i
print(s)
# print(n*(n+1)//2)


# 6. Factorial of a Number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)


# 7. Sum of m to n Numbers
m = int(input("Enter m value: "))
n = int(input("Enter n value: "))
s = 0
for i in range(m,n+1):
    s += i
print(s)


# 8. Product of m to n Numbers
m = int(input("Enter m value: "))
n = int(input("Enter n value: "))
prod = 1
for i in range(m, n+1):
    prod *= i
print(prod)


# 9. Print Factors of a Number
n = int(input("Enter a number: "))
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=" ")


# 10. Count of Factors
n = int(input("Enter a number: "))
c = 0
for i in range(1, n):
    if n%i == 0:
        c += i
if c == n:
    print("Perfect number")
else:
    print("Not a perfect number")


# 11. Prime Number Check
n = int(input("Enter a number: "))
if n<=1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, n):
        if n%i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not a prime number")


# 12. Even Numbers from m to n
m = int(input("Enter m value: "))
n = int(input("Enter n value: "))
even_count = 0
odd_count = 0
for i in range(m, n+1):
    if i%2 != 0:
        odd_count += 1
    else:
        even_count += 1
print(f"Even = {even_count}, Odd = {odd_count}")


# 15. Reverse a String
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


# 17. Sum of Digits
n = int(input("Enter a value: "))
temp = n
s = 0
while temp>0:
    x = temp%10
    s = (s*10) + x
    temp //= 10
print("Palindrome" if s==n else "Not a palindrome")
 


# 22. Count Vowels in String
s = input("Enter a string: ")
consonants = 0
vowels = 0
for i in s:
    if i not in "aeiou":
        consonants += 1
    else:
        vowels += 1
print(f"Vowels = {vowels}, Consonants = {consonants}")





# 26. Neon Number Check
n = int(input("Enter a number: "))
sq = n**2
c = 0
while sq > 0:
    j = sq%10
    c += j
    sq //= 10

if c == n:
    print("Neon number")
else:
    print("Not a neon number")



# 27. Strong Number Check
def factorial(n) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
temp = n
s = 0
while temp > 0:
    x = temp%10
    s += factorial(x)
    temp //= 10
print("Strong number" if s == n else "Not a strong number")



# # 28. Harshad Number Check
n = int(input("Enter a number: "))
temp = n
s = 0
while temp > 0:
    x = temp % 10
    s += x
    temp //= 10

if n % s == 0:
    print("Harshad number")
else:
    print("Not a Harshad number")


# 29. Fibonacci Series
n = int(input("Enter a number: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b
