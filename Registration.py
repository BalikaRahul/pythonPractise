def registration():
    name =input('enter your name: ')
    phone =input('enter your Phone number: ')
    email =input('enter your email: ')
    address =input('enter your address: ')
    password =input('enter your password: ')
    retype =input('retype your password: ')
    if password == retype: 
        print(f'{name} ,{phone} , {email} , {address}, {( "*" * (len(password)-2))}{password[-1:-5:-1]}')
        validation(name,phone,email,password,address)
    else: 
        print('password is mismatch')
    
def validation (name,phone,email,password,address):
    if name.isalpha():
        if len(phone)== 10 and phone.isdigit():
            if (email.endswith('.com') or email.endswith('in')) and email.count("@") ==1:
                lower = 0
                upper =0
                symbol =0
                if len(password) >=8:
                    for i in password:
                        if i.isupper():
                            upper+=1
                        elif i.islower():
                            lower+=1
                        elif i =='@' or i =="#" or i == '$' or i == '%' or i == '&' or i=='*' :
                            symbol+=1
                    if lower >=1 and upper >=1 and symbol>=1:
                        username = email.split("@")[0]
                        print(f'your username is {username}')
                        login (username,password)
                    else:
                        print(f'your password is too weak: {password}')
                else:
                    print(f'your password should have atleast 8 character but have only :{len(password)}')
            else:
                print('your email id is invalid')
        else:
            print('phone number should have only numberic values',phone)
    else:
        print('name should have only alphabets:',name)

def login(username ,password):
    count =0 
    while True:
        if count <=3:
            UserName = input('enter your username: ')
            Password =input('enter your Password: ')
            if username == UserName and password == Password:
                print(f'{"="*5}welcome to home page! {"="*5} ')
                break

            else: 
                print("incorrect username or password")
            count+=1
        elif count >3:
            print('you have reached your limit! ')
            break
registration()

