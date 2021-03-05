import math
from math import *

#Zadanie1
#int
a, b=1, 2
#float
c, d=1.1, 2.1
#complex
e, f=1+1j, 2+2j
#string
str1, str2="string1","string2"

print(a,b,c,d,e,f,str1,str2)

#Zadanie2
a=2
b=2
dodawanie = a + b
print(dodawanie)
odejmowanie = a + b
print(odejmowanie)
mnozenie = a * b
print(mnozenie)
dzielenie = a / b
print(dzielenie)
potegowanie = a**b
print(potegowanie)
pierwiastkowanie = a**(1/b)
print(pierwiastkowanie)
#Zadanie3
a = 1
dodawanie, odejmowanie, dzielenie, mnozenie, potegowanie, reszta=1,2,3,4,5,6
dodawanie+=a
odejmowanie-=a
dzielenie /=a
mnozenie *=a
potegowanie **=a
reszta%=a
print(dodawanie, odejmowanie, dzielenie, mnozenie, potegowanie, reszta)
#Zadanie4
var1 = math.e **10
var2 = log(5+sin(8)**2)**1/6
var3 = floor(3.55)
var4 = ceil(4.80)
print(var1, var2, var3, var4)
#Zadanie5
firstName = "ARKADIUSZ"
secondName = "KOWALSKI"
print(firstName.capitalize() + " " + secondName.capitalize())
#Zadanie6
tekst = "I find a way to block it, I go la la na na"
print(tekst.count(" la"))
#Zadanie7
drugaLitera = "Druga litera"
ostatniaLitera = "Ostatnia litera"
print(drugaLitera[1], ostatniaLitera[-1])
#Zadanie8
tekst = "I find a way"
print(tekst.split())
#Zadanie9
a, b, c =100, 1.01, "Tekst"
print("Szesnastkowy: %(a)x Float: %(b)f String: %(c)s" %{'a':a, 'b':b, 'c':c})