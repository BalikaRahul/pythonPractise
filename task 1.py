# def problem1(anything):
#     anything = anything.replace(" ","")
#     return anything
# anything =input('enter your string: ')
# print(problem1(anything))
# def problem2(anything):
#     anything=anything[::-1]
#     return anything
# anything =input('enter your string: ')
# print(problem2(anything))
# def problem3(anything):
#     anything = anything.replace(" ","")
#     anything=anything[::-1]
#     return anything
# anything =input('enter your string: ')
# print(problem3(anything)) \

# def problem14(anything):
#     result =''
#     for i in range(len(anything)):
#         if anything[i].isdigit():
#             result+=anything[i]
#     return result
# anything =input('enter your string: ')
# print(problem14(anything))

# def problem17(anything):
#     if len(anything)<8:
#         return 'your password is too weak beacuse the length of your password has less than 8 character '
#     else:
#         for i in range(len(anything)):
#             if anything[i].isupper():


# def problem18(anything):
#     result =''
#     dep=''
#     for i in range(len(anything)):
#         if anything[i] not in result:
#             result+=anything[i]
#     return result
# anything =input('enter your string: ')
# print(problem18(anything))

# def problem19(anything):
#     result =''
#     dep=''
#     for i in range(len(anything)):
#         if anything[i] not in result:
#             result+=anything[i]
#         else:
#             dep+=anything[i]
#     return dep
# anything =input('enter your string: ')
# print(problem19(anything))
def nothing(age):
    print(f'{age}')
nothing(int('23'))