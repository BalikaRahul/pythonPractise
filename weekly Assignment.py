student_names = ["Aarav", "Bhavna", "Chetan", "Diyya", "Esha"]
student_marks = [45, 88, 92, 35, 75]
print(f'the total number student in the class: {len(student_names)}')
print(f'The Top scorer of the Class is {student_names[2]} with the marks of {student_marks[2]}')
for i in range(len(student_names)):
    if student_marks[i] >= 80:
        print(f'{student_names[i]} has secured A with marks : {student_marks[i]} ')
    elif 50<=student_marks[i]<=79:
        print(f'{student_names[i]} has secured B with  marks : {student_marks[i]} ')
    elif student_marks[i] <50:
        print(f'{student_names[i]} has failed in the exam  and secured  : {student_marks[i]} ')
total =0 
avg =0
for i in range(len(student_marks)):
    total+=student_marks[i]
avg = total/len(student_marks)
print( "the average marks of the class is : ",avg)
fail =0
Pass =0
for i in range(len(student_marks)):
    if student_marks[i] >= 50:
        Pass+=1
    else:
        fail+=1
print('the total nubmer of student pass in the exam is: ',Pass)
print('the total nubmer of student fail in the exam is: ',fail)
print('='*50)









print('='*50)
#  Task 2 
vip_list = ["Rahul", "Ananya", "Sneha", "Vikram"]
regular_list = ["Amit", "Pooja", "Rohan", "Kavya"]
name =input("Enter your name: ")
age = int(input('enter the age: '))
if name in vip_list and age >=18:
        print(f'{name} Access Granted to VIP Zone ')
elif name in vip_list and age <18:
        print(f'{name} found in VIP Zone but you do have Access because your age lessthan 18{age}')
elif name in regular_list and age >=18:
        print(f'{name} Access Granted to Regular Zone ')
elif name in regular_list and age <18:
        print(f'{name} found in regular Zone but you do have Access because your age lessthan 18{age}')
else:
        print(f'{name} is not found in both list your ticket is  invalid and comes under Unknown Pass Category you do not have any access  ')
print('='*50)







print('='*50)
#Task 3 
n=int(input('enter the number: '))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j ==0 or j == n-1:
            print('*',end =' ')
        else:
            print(' ',end =' ')
    print()
print('='*50)

# pattern 2
print('='*50)
n=int(input('enter the number: '))
num =0
for i in range(n):
    for j in range(i+1):
        num+=1
        print(num,end = ' ')
    print()
print('='*50)



#pattern 3
print('='*50)
n = int(input('enter the number: '))
for i in range(n):
    for space in range(i+1):
        print(' ',end=' ')
    for j in range(2*(n-i-1)-1):
        print("*",end =' ')
    print()
for i in range(1,n):
    for space in range(n-i-1):
        print(' ',end =' ')
    for j in range(2*i+1):
        print('*',end=' ')
    print()