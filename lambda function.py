# def division(a,b):
#     if b==0:
#         return 'the value of b is zero'
#     return f" the value of a/b {a/b}"
# a = int(input('enter the value of a: '))
# b = int(input('enter the value of b: '))
# print(division(a,b))



# def loginSystem(user,password):
#     if user == "admin" and password=='python123':
#         return "Login successfull"
#     else:
#         return 'Invalid Credentials'
# print(loginSystem('admin','python123'))

# def register(age):
#     if age <18:
#         return f'registration is failed because you dont have enough age to register. register after{18-age} years'
#     else:
#         return f"Registration Successful"
# age = int(input('enter your age: '))
# print(register(23))


# square =lambda a :a*a
# number = int(input('enter the number: '))
# print(f'the square of the given {number} is {square(number)}')


# largest = lambda a,b: b if a<b else b
# a =int(input('enter your number: '))
# b =int(input('enter your number: '))
# print (f'the largest number between {a,b} is {largest(a,b)}')


# evenOrNot = lambda a: "even" if a%2==0  else "odd"
# number = int(input('enter the number: '))
# print(f'the given {number} is {evenOrNot(number)}')

# grade = lambda marks: "pass" if marks>=35  else "fail"
# marks = int(input('enter the number: '))
# print(f'the  student who has obtained {marks} is {grade(marks)}')

# def greet(name):
#     return f'hello {name}'
# def execute(name):
#     print(greet(name))
# name =input('enter your name: ')
# execute(name)




# def add (a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return (a*b)
# def selectOperation(operation,a,b):
#     if operation =='add':
#         print(add(a, b))
#     elif operation == "sub":
#         print(sub(a, b))
#     elif operation == "mul":
#         print(mul(a, b))
#     else:
#         print("Invalid operation")
# operation = input('enter the operation: ')
# a=int(input(('enter the number: ')))
# b=int(input(('enter the number: ')))
# selectOperation(operation,a,b)


# def welcome(name):
#     return f'hello {name}'
# def display(name):
#     print(welcome(name))
# name =input('enter your name: ')
# display(name)


# square = list(map(lambda a:a*a, [i for i in range(1,11)]))
# print(square)


names = ["rahul", "anita", "john", "kiran"]
upper=list(map(lambda i:i.upper(),names))
print(upper)

# marks = [60, 72, 81, 45, 90]
# bonus_marks = list(map(lambda i:i+5,marks))
# print(bonus_marks)

# cities = ["Delhi", "Mumbai", "Chennai", "Hyderabad"]
# word_len = list(map(lambda i: len(i), cities))
# print(word_len)

# temperatures = [0, 10, 20, 30, 40]
# convert = list(map(lambda i: ((i*9/5)+32),temperatures))
# print(convert)

