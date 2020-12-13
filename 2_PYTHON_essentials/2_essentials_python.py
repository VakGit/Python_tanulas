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

szam=pow(2,4)#pow a hatványozás
#szam=pow(2,4000) ez már nagyon nagy szám lenne
print(szam)

"""
-----------------------------------------------------------------------
***3_STRING***
-----------------------------------------------------------------------

___**SLICING**____ 
    - KIIRATAS: 
               egy tömbrész részhalmazát adja vissza ->>
              
              szoveg[kezdőpozició : zaropozicio+1 : lépésköz] 
  
A string felfoghagtó egy tömbként , amelynek azonosítói vannak(indexei) pozitiv és negativ index
pld:
"A L M A"
 
  0 1 2 3  -> 0-től a végéig 3
 
 -4-3-2-1 -> -1-től az elejéig -4

"""
#MINTA A SLICING-RA 
#a minta szöveg
szoveg="Darabolás!"

#teljes változó kiirása nem slicing változóként
print (szoveg)

#teljes valtozo kiirasa slicing változóként  az elejétől a végéig , 
#ha nem adjuk meg a végső értéket akkor végig megy a szövegen
#alapértelmezet lépésköz 1 
print(szoveg[0::1])
print(szoveg[0::])
print(szoveg[-len(szoveg): :]) #a hosszát a szövegnek meghatároztam, majd negatív indexként megadtam és 1-et hozzáadva ki lett írva a szöveg

#a végétől az elejéig, figyelj hogy -1 a lépésköz ilyenkor 
print(szoveg[-1::-1])
print(szoveg[::-1]) #ha -1 a lépésköz úgy felttelezi, hogy a végéről visszafelé haladsz , nem kell a többi paraméter

#az első három betű kiíratása !! 0-val kezd és a 3. indexet már nem írja ki 
print(szoveg[0:3:])
print(szoveg[:3:])

#az utolsó három betű kiíratása visszafelé
print(szoveg[-1:-4:-1])
#az utolsó három betű kiíratása normál
print(szoveg[len(szoveg)-3::])
print(szoveg[-3::])

#minden második betű kiírása
print(szoveg[1::2])

#az ötödik betű kiírása
print(szoveg[4])
print(szoveg[-len(szoveg)+4]) #a pozíció -hossz-normálpozício

"""Rövid program írása slicing bemutatására
-------------------------------------------

-------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
MEGJEGYZÉS: A megkezdett kódrészlet kigészítésa TAB billenbtyű leütésének hatására, ennek a BEÁLLÍTÁSA 
1. lépés Beállítások 
2. lépés OPEN SETTING (JSON)
3. lépés beillesztés a paraméterekhez ["editor.snippetSuggestions": "top"] beállítást
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

Cél:
...............
PALINDROM PÉLDA 
...............
...............
oda-vissza megegyezik e a szó 
pld.
görög ua. oda-vissza olvasva
"""
szoveg="agörög"
mirror=szoveg[::-1]
#print(mirror)
if szoveg==mirror:
  print(f"::{szoveg}:: szó egy palindrom.")
else:
  print(f"::{szoveg}:: szó NEM palindrom.")


"""--------------------------------------------------------------------
FIGYELEM , VIGYÁZAT!!!!!
A STRING IMMUTABLE !!!!!
----------------------------------------------------------------------
A STRING minden értékadásnál új memória címet kap,
 a stringen végrehajtott műveletek függvények (pld. szoveg.replace())használata esetén ,
 automatikusan nem íródnak át az változók !!!!

PÉLDÁK:
"""
#ÚJ MEMÓRIA CÍM bemutatása
#változó id-nek bemutatása
szoveg="alma_1"
print(f"{szoveg}-> szoveg id:{id(szoveg)} ")
#változó id-nek bemutatása
szoveg="alma_2"
print(f"{szoveg}-> szoveg id:{id(szoveg)} ")
#látható hogy két különböző hely a memóriában 


#SZÖVEGEN FÜGGVÉNNYEL TÖRTÉNŐ VÁLTOZTATÁS HELYES MÓDJA 
#a szöveg függvénnyel történő manipulása, a palindrom példán keresztül
#alaptézis
#---------
szoveg="indul a görög aludni" #a betűk tekintetében palindrom egyébként nem 
mirror=szoveg[::-1]
#print(mirror)
if szoveg==mirror:
  print(f"::{szoveg}::  egy palindrom.")
else:
  print(f"::{szoveg}::  NEM palindrom.")
#azaz a szóközök miatt nem az

#módosítása az alapfeltételezésnek 
#ha nem vesszük figyelembe a szóközöket, akkor palindrom a szöveg 
szoveg="indul a görög aludni" 
#kell egy függvény amely kiveszi a SZÖVEGBŐL a szóközöket
szoveg.replace(" ", "") #.replace(mit,mire,hányszor)
#nézzük mi lesz
print(f"::{szoveg}:: ez még az eredeti szöveg!?")#nem lesz jó mert még az eredetiértéket írja ki 
#mivel a string IMMUTABLE az eredeti változó id. a régi értékre mutat; a változások új helyre kerültek!!!
#javítsunk !!!!
#NAGYON FONTOS A VÁLTOZÓK MANIPULÁSA CSAK AZ EREDETI VÁLTOZÓBA BEÍRVA LÉPNEK ÉLETBE
#LASD
szoveg=szoveg.replace(" ","")
print(f"::{szoveg}:: a szöveg így már jó:)")
mirror=szoveg[::-1]
#print(mirror)
if szoveg==mirror:
  print(f"::{szoveg}::  egy palindrom.")
else:
  print(f"::{szoveg}::  NEM palindrom.")

#NAGYON VIGYÁZNI ÍGY NAGYOT LEHET HIBÁZNI 

"""
-------------------------------------
**FIGYELEM !!!! A LISTA MUTABLE !!!**
-------------------------------------
>A rajta végrehajott fv-ek hatására a lista az eredeti helyükön változik meg
"""

#egy lista elemeinek megfordítása 
lista=[1,2,3,4]
print(lista)
lista.reverse()#.reverse() megfordítja az elemek sorrendjét
print(lista)

"""
-----------------------
**TIPIKUS STRING FV_EK**
------------------------
"""

szoveg="Indul a gorog aludni"
#szóközöket törlöm és kiírom, ez a c#-ban egy fv. amely egy uj stringet ad vissza 
print(szoveg.replace(" ",""))

#megforditva kiirom
print(szoveg[::-1])

#a substring x-ik pozicióját kapjuk meg
print(szoveg.find("gorog"))

#nagybetű
print(szoveg.upper())

#kisbetű "\" uj sor
print(f"{szoveg.lower()}\n\n")

#megszámolja mennyi substring van a szövegben pld. o-betű
print(szoveg.count("o"))

#szoveg hossza
print(len(szoveg))

#szöveg listába rakása alpertelmezetten a szóköz a határoló .split() fv.
lista=szoveg.split()
print(lista)

#beépített help 1. az adattipusú változón meghívható fv-ek
#másképpen:  egy objektumon értelmezett összes attributum vagy függvény
print(dir(str))
print('\n')#uj sor , ures sor 
print(dir(int))

#beépített help 2. egy specifikus fv. -hez tartozó leírás
print(help(str.count))