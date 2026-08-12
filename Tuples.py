# #task 1 
movie =[]
count=0
total =0
while True:
    movie_name=input('enter the movie name: ')
    seat_number=input('enter the seat: ')
    print("The price of the single ticket is '250'")
    ticket=int(input('enter how many tickets you need: '))
    moreTicket=input('do you need more tickets enter (yes or no): ')
    person =(movie_name,seat_number,ticket)
    count+=ticket
    total=count*250
    movie.append(person)
    if moreTicket == 'no':
        print('the total number of tickets are:',count)
        print('the total cost of the tickets are:',total)
        for i in range(len(movie)):
            print(movie[i])
        break


# Task 2
regi=set()
while True:
    student=input('enter the student name: ')
    if student in regi:
        print(f'{student} you have already registered')
    regi.add(student)
    if student == 'done':
        print('the total number of registered students are:',len(regi))
        print('final registered students are ')
        print(regi)
        break
    print(regi)
   
        

    