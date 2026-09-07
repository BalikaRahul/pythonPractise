# import random

# def passwordGenerator(password):
#     capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     small =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     symbol=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
#     while len(password)<8:
#         password.append(random.choice(capital))
#         password.append(random.choice(small))
#         password.append(random.choice(symbol))
#     random.shuffle(password)
#     password = "".join(password)
#     return password
# password=[]
# print(passwordGenerator(password))
# Generate characters from any start letter to end letter
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

print(alphabet)