import pyperclip
import secrets
import random
# długość hasła
# losowanie liczby
def DrawANumber():
    number = secrets.randbelow(9)
    return number
# losowanie dużych liter
def CapitalLetter():
    x = 0
    wielka_litera = []
    for i in range(65, 91):
        litera = chr(i)
        x += 1
        wielka_litera = litera
    return wielka_litera
biglitera = CapitalLetter()
def Lowercase(n: int):
    small = []
    index = 0
    while index <= n:
        for i in range(65, 91):
            litera = chr(i)
            if litera != biglitera:
                small.append(litera.lower())
                index += 1
    return small
# losowanie hasła
def passwordRandomization(big):
    n = int(input("Podajdługość hasła:"))
    lower = Lowercase(n-2)
    number = DrawANumber()
    password = ''

    index = 0
    while n != 0:
        los = random.randint(1, n)
        if los % 2==0:
            password = password + lower[index]
            index += 1
        elif los % 3 == 0:
            if big != '':
                password = password + big
                big= ''
        else:
            if number != -1:
                password = password + str(number)
                number = -1
        n -= 1
    print(password)
    pyperclip.copy(password)
    return password

passwordRandomization(biglitera)
