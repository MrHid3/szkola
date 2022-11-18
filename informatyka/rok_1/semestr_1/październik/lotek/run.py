from random import randint as rand

numbers = []
payout = 0

print("Hello adventurer, what are your numbers?")
while len(numbers) < 6:
    c = int(input())
    if c not in numbers:
        numbers.append(c)
    else:
        print("You already chose this number!")
print("How many times to you want to play?")
playtimes = int(input())

for i in range(playtimes):
    winning = []
    sum = 0
    payout -= 5
    for i in range(6):
        a = rand(1,49)
        if a not in winning:
            winning.append(a)
    for element in numbers:
        if element in winning:
            sum += 1
            print(f'\033[92m',element,"hitted!")
        else:
            print(f'\033[91m',element,"missed!")
    if sum == 3:
        payout += 10
    elif sum == 4:
        payout += 1000
    elif sum == 5:
        payout += 3500
    elif sum == 6:
        payout += 1000000
    
if payout > 0:
    print(f'\033[92m',"You won", payout,"dolars!")
elif payout == 0:
    print("You won nothing!")
else:
    print(f'\033[91m',"You lost", -payout,"dolars!")