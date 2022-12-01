import random

password = []
passwordstr = ""

long = int(input("Your password's lenght: "))

for i in range(long):
    password.append(str(chr(random.randint(33,126))))

random.shuffle(password)

for i in range(len(password)):
    passwordstr += password[i-1]

print("This is your password: " + passwordstr)