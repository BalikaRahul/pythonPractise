Aadhar={
    'FirstName':'Luffy',
    'LastName':'Monkey . D',
    'FullName':'Monkey.D.Luffy',
    'age':18,
    'aadhar':3879779243787987,
    'email':'monkeydluffy2@gmail.com',
    'Father':'Monkey .D . Dragon',
    'Address':{
        'Village':'Foosha',
        'city':'Dawn island',
        'kingdom':'East Blue'
    }
}
FirstName=input('enter your FirstName: ')
Aadhar['FirstName'] = FirstName
LastName=input('enter your LastName: ')
Aadhar['LastName'] = LastName
FullName = input('enter your FullName: ')
Aadhar['FullName']=FullName
age=int(input('enter your age: '))
Aadhar['age']=age
aadhar =int(input('enter your aadhar number: '))
Aadhar['aadhar'] =aadhar
email=input('enter your email: ')
Aadhar['email'] =email
FatherName = input('enter your Father Name: ')
Aadhar['Father'] = FatherName
village = input('enter your village name: ')
Aadhar['Address'] ={"village":village}
city =input('enter your city name: ')
Aadhar['Address'] ={'city':city}
kingdom=input('enter your kingdom: ')
Aadhar['Address'] ={'kindom':kingdom}

print(Aadhar)