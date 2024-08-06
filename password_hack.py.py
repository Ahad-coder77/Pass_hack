import random
import string


input = str(input("Enter your strong password in letters and digits : "))

add = string.ascii_letters + string.digits
password = ""

while password != input:
    password = ""
    
    while len(password) != len(input):
        
        password += random.choice(add)
        print("Generated password:", password)
        
print("Is your password is : ", password)




