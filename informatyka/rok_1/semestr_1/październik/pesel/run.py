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

#Plec
if int(pesel[9])%2 == 1:
    plec = 1
else:
    plec = 0

#Suma kontrolna
suma_kon = 10 - ((int(pesel[0]) + int(pesel[1])*3 + int(pesel[2])*7 + int(pesel[3])*9 + int(pesel[4]) + int(pesel[5])*3 + int(pesel[6])*7 + int(pesel[7])*9 + int(pesel[8])*1 + int(pesel[9])*3) % 10) % 10

if pesel[10] != suma_kon:
    print("nieprawidlowy pesel")

#Podsumowanie
else:
    print(f"Ta osoba urodziła się {dzien} dnia {miesiac} miesiąca {rok} roku")
    if plec == 1:
        print("Jest to mężczyzna")
    else:
        print("Jest to kobieta")