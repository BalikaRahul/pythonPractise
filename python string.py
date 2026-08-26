print('='*80)
print("CODEHUB USER REGISTRATION")
print('='*80)
full_name = input('enter your full name: ')
email=input('enter your email: ')
phone_number =input('enter your phone_number: ')
city= input('enter your city name: ')
favourite_technology=input('enter your favourite technology: ')
skill=input('enter your skill  separated by comma: ')
full_name = full_name.title()
email=email.lower()
favourite_technology=favourite_technology.casefold()
user_name = email.split("@")[0]
print('processing profile..')


# skill.split(",")
print(f'skill: {skill.replace(","," | ")}')

developer_id = full_name.split()[0]+city[0]+favourite_technology
security = favourite_technology.casefold()[0:2]+user_name[0:3]+city[0:4]
print(f""" 
{'='*80}

PROFILE
{'='*80}
Name :{full_name}
Username :{user_name}
Email :{email}
Phone :{phone_number}
City :{city}
Technology :{favourite_technology}
Skills :{skill}
{'='*80}
EMAIL ANALYSIS
{'='*80}
Starts with username : {email.startswith(user_name)}
Ends with .com :{email.endswith(".com")}
@ position :{email.find("@")}
Number of dots :{email.count(".")}
{'='*80}
DEVELOPER INFORMATION
{'='*80}
Developer ID :{developer_id}
Security Key :{security}
""")