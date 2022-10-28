print("Podaj PESEL")
pesel = input()
pesel = list(pesel)
stulecie = int()

#Miesiąc urodzenia
lm = int(pesel[2] + pesel[3])
if (1 <= lm - 80 <= 12):
    miesiac = lm - 80
    stulecie = 18
elif (1 <= lm <= 12):
    miesiac = lm
    stulecie = 19
elif (1 <= lm - 20 <= 12):
    miesiac = lm - 20
    stulecie = 20
elif (1 <= lm - 40 <= 12):
    miesiac = lm - 40
    stulecie = 21
elif (1 <= lm - 60 <= 12):
    miesiac = lm - 60
    stulecie = 22
else:
    print("niepoprawny pesel")
    exit()


#Rok urodzenia
rok = (stulecie*100)+int(pesel[0] + pesel[1])

#Dzień urodzenia
dzien = int(pesel[4]+pesel[5])