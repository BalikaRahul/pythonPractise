# def student_detail(name,age,course):
#     return f"{name} {age} {course}"
# name =input('enter your name: ')
# age =int(input('enter your age: '))
# course =input('enter your course name: ')
# print(student_detail(name,age,course))
# def employee_salary(employee_name,salary =25000):
#     salary += salary*20//100
#     return f"{employee_name} {salary}"
# employee_name=input('enter your name: ')
# salary = int(input('enter your salary: '))
# print(employee_salary(employee_name,salary))
def movie_info(movie_name,hero,rating):
    return f""" movie name:{movie_name}
hero:{hero}
rating:{rating}
"""
movie_name = input('enter your movie_name: ')
hero = input("enter your hero_name: ")
rating = float(input('enter your movie_rating: '))
print(movie_info(movie_name,hero,rating))