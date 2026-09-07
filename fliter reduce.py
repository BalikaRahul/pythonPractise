# even = [12, 7, 5, 18, 20, 9, 14]
# even_number = list(filter(lambda i:i%2==0,even))
# print(even_number)
# marks = [25, 40, 89, 30, 75, 55, 18]
# pass_marks=list(filter(lambda x: x>=35,marks))
# print(pass_marks)
# numbers = [-10, 15, -8, 20, 0, 35, -2]
# pos=list(filter(lambda x:x>0,numbers))
# print(pos)
# words = ["cat", "elephant", "dog", "computer", "pen", "keyboard"]
# length=list(filter(lambda x:len(x)>5,words))
# print(length)
# numbers = [10, 12, 15, 18, 20, 23, 25, 31]
# mul5=list(filter(lambda x:x%5==0,numbers))
# print(mul5)
# from functools import reduce
# numbers = [10, 20, 30, 40, 50]
# Sum =reduce(lambda x,y:x+y,numbers)
# print(f'The sum of the given number:{Sum}')    
# numbers = [2, 3, 4, 5]
# product =reduce(lambda x,y:x*y,numbers)
# print(f'The product of the given numbers:{product}')
# numbers = [45, 12, 98, 67, 21]
# largest =reduce(lambda x,y:x if x>y else y,numbers)
# print(f'the largest number in the array is {largest}')
# numbers = [45, 12, 98, 67, 21]
# smallest =reduce(lambda x,y:y if x>y else x,numbers)
# print(f'the smallest number in the array is {smallest}')
# words = ["apple", "banana", "kiwi", "watermelon", "grapes"]
# longest_word =reduce(lambda x,y:x if len(x)>len(y) else y,words)
# print(f'the longest_word  in the array is {longest_word}')
def Nothing(name,age,marks,section):
    return name,age,marks,section
name = input('enter your name')
age=int(input(' : '))
marks=input(': ' )
print(Nothing(age=age, name=name, marks =marks,section='a'))