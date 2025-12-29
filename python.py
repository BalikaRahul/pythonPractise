#what is HTTP. what is client and sever . what is the difference between GET POST . what is the request and response . what are the types of requests.
def even(num):
    if(num%2==0):
        return "even"
    else:
        return "not a even number"
num =int(input("enter the number"))
result= even(num)
print(result)