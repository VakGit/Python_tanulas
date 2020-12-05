# -*- coding: utf-8 -*-
"""
**1_első lépések**
---
minden változó egy osztály  és dinamikusan generálódik a tipusa , nem a stack-ban hanem a heap-ban jön létre a változó
"""

number=12
print(type(number))
number=12.1
print(type(number))
number="Hello"
print(type(number))

"""**2_Python3 Basic syntax**
------------------------------------------------------------------------------------------------------------------------------------------
***Számok:***
mindegyik egy osztály -> int, float, complex (csak ennyi és nem több, **nincs túlcsordulás a heap miatt,** ezért nincs double , long stb.) 
> ***műveletek***: +,-,/,*,//-div(egész osztás), %-mod(maradék osztás)
---------------------------------------------------------------------------------------------------
**A változó minden értékadáskor új memóriacímet foglal le** , az előtte levő címet nulláza (talán?!)
"""

# Int
number = 12
#formatstring a print-nél ; print(f"szöveg {valtozo} szoveg stb. {valtozo)")
print(f" Integer: {number}, memory address: {id(number)}")
#egészosztás
print(type(number))
print(number//24)
print(-number//24)
print (number//-24)
print(-number//-24)
#nesze neked , negatív számok esetén a negatív végtelen felé kerekít,
#majd utána nézni?!!!
#-------
#maradékosztás
print("-----")
print(number%16)
print(-number%16)
print(number%-16)
print(-number%-16)
#érti a fene, hogy mit csinál ?!!!

# Float
number = 16.1
#formatstring a print-nél ; print(f"szöveg {valtozo} szoveg stb. {valtozo)")
print(f" Float: {number}, memory address: {id(number)}")

print(type(number))

# Complex
number = 3 + 4j
print(f" Complex: {number}, memory address: {id(number)}") 
#formatstring a print-nél ; print(f"szöveg {valtozo} szoveg stb. {valtozo)")

print(type(number))

"""Az "id" az egy egyedi belső azonosító, hasonlóan mint egy memóriacím, de nem igazi memóriacím, nem lehet rajta keresztül válotozóra hivatkozni, mintha egy pointer lenne.
https://docs.python.org/3.5/library/stdtypes.html#numeric-types-int-float-complex

Pythonban az Int is egy osztály, így nincs "egyszerű típus", az Int nincs a regiszterek méretéhez kötve mint a "C" típusú nyelvekben (32, 64bit stb.), csak a memóriánk mérete szab határt, így túlcsordulás sincs.
Minden a memóriában foglalódik le (a heapen és nem a stacken) - összehasonlítva C++-al pl. nem egy mutatót hozunk létre és annak tipusának megfelelő helyet foglalunk le, hanem egyből az egész memória terület lesz maga az objektum, típustól függetlenül.
------------------------------------------------------------------------------------
A változók értékadása: speciális esetben egymás után felsorolva értékek adhatók nekik.
"""

a,b=8,3
print(a//b)
a,b,c,d,e=8,2.13,"hello",{1,4,5,6},[7,8,9,10]
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

"""**Nincs túlcsordulás,**
----------------------------------------------------------------------
végtelen értéke lehet a változónak,  csak a memória mérete szab határt
"""

szam=pow(2,4000)#pow a hatványozás
print(szam)