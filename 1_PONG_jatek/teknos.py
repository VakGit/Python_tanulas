#beolvasása egy meglévő osztálynak 
import turtle

#ABLAK létrehozása

ablak = turtle.Screen()
#ablak mérete
ablak.setup(width=800, height=600)
#ablak háttere 
ablak.bgcolor("black")
ablak.title("PONG")
#kikapcsolja a teknos objektum animálását megjelenését kirajzolását az ablakon belül , egy nem negativ szammal
ablak.tracer(0)

#egy hosszú megjegyzés jön - un. többsoros , három időzőjel elején-végén
"""
#egy teknőssel rajzolunk 

petiteknos=turtle.Turtle()

#petiteknos.shape("turtle")
#Megváltoztatjuk a toll alakját
petiteknos.shape("square")
#a méretét állítjuk
petiteknos.shapesize(stretch_wid=5, stretch_len=1)
#a színét
petiteknos.color("green")
#a tollat felemeljukm nem rajzol semmit csak az alak mozog 
petiteknos.penup()

#a toll sebessege
petiteknos.speed(1)
#toll iranya és irasanak hossza
petiteknos.forward(200)
petiteknos.right(90)
petiteknos.forward(200)
petiteknos.right(90)
petiteknos.forward(200)
petiteknos.right(90)
petiteknos.forward(200)
petiteknos.right(90)
"""

# BAL oldali utő létrehozása

bal_uto=turtle.Turtle()
bal_uto.speed(0)
bal_uto.shape("square")
bal_uto.shapesize(stretch_wid=5, stretch_len=1)
bal_uto.color("blue")
bal_uto.penup()
#pozicio - bal + jobb, X utána y 
#koordináta rendszer origója az ablak középpontja
bal_uto.goto(-350,0)

#JOBB oldali utő létehozása 

jobb_uto=turtle.Turtle()
jobb_uto.speed(0)
jobb_uto.shape("square")
jobb_uto.shapesize(stretch_wid=5, stretch_len=1)
jobb_uto.color("red")
jobb_uto.penup()
#pozicio -jobl + jobb, X utána y 
#koordináta rendszer origója az ablak középpontja
jobb_uto.goto(350,0)

#LABDA objektum létrehozása
labda = turtle.Turtle()
labda.speed(5)
labda.shape("circle")
#ha a labdanak nem adunk meretet alapbol 1 lesz
#labda.shapesize(stretch_wid=1, stretch_len=1)
labda.color("yellow")
labda.penup()
#pozicio -jobl + jobb, X utána y 
#koordináta rendszer origója az ablak középpontja
labda.goto(0,0)
#labda objektumon belül saját valtozokat hozunk letre 
labda.valtozasX = 1
labda.valtozasY = -1

#PONTSZÁM objektum létrehozása
jobb_pontszam = 0 #számlálók
bal_pontszam = 0
pontszam = turtle.Turtle()
pontszam.speed(0)
pontszam.color("white")
pontszam.penup()
pontszam.hideturtle()
pontszam.goto(0,260)
#pontszam kiiratása
pontszam.write(f"Jobb játékos:{jobb_pontszam} Bal játékos: {bal_pontszam}", align="center",font=("curier",23,"normal"))


#FÜGGVÉNYEK KÉSZÍTÉSE 
#def nev parameter :        nincs zárójel !!!!  a fordító a törzs befejezését onnan tudja, hogy egy ures sort utána teszünk
#ütők mozgásai
def bal_uto_fel():  
    y = bal_uto.ycor()
    y+=30 #y = y+30
    bal_uto.sety(y)

def bal_uto_le():  
    y = bal_uto.ycor()
    y-=30 #y = y-30
    bal_uto.sety(y)

def jobb_uto_fel():  
    y = jobb_uto.ycor()
    y+=30 #y = y+30
    jobb_uto.sety(y)

def jobb_uto_le():  
    y = jobb_uto.ycor()
    y-=30 #y = y-30
    jobb_uto.sety(y)

#billentyűzet figyelés , az ablakban meghivunk egy függvényt, paraméter (fv, billentyű)
ablak.onkey(bal_uto_fel, "w")
ablak.onkey(bal_uto_le, "s")
ablak.onkey(jobb_uto_fel, "o") #"Up"
ablak.onkey(jobb_uto_le, "l")  #"Down"


#be kell kapcsolni a billentyűzet figyelést az ablakban 
ablak.listen()


#ne szaladjon el az ablak , ezért végtelen ciklus jön
"""
#csak a program lelövésével lehet kilépni
while True:
    pass
"""

#A JATEK LEKEZELÉSE EGY CIKLUSBAN
#normál módon kilehet lépni alt-x stb.
#cikluson belül a törzsnek 4 db (négy) space-vel beljebb kell kezdődni, ha nem akkor hiba !!!!!!
#függőlkeges pozícióba állítom a labdát 
#labda.valtozasX = 0
#vízszintes pozícióba állítom a labdát 
#labda.valtozasY = 0

while True:
    ablak.update() #ablak frissítése 
    
    labda.setx(labda.xcor() + labda.valtozasX)
    labda.sety(labda.ycor() + labda.valtozasY) # nem tudom miért jó üres sor van vége kellene hogy legyen a ciklusnak 

    #LABDA FÜGGŐLEGES MOZGÁSÁNAK LKEZELÉSE
    #az ablak tetejéről pattanjon vissza 
    if labda.ycor() > 288: #300 lenne a jó de a labdának van kiterjedése ezért kisebb értéket adunk meg
        labda.sety(288)
        labda.valtozasY *=-1 # a valtozo ertekének előjele megváltozik

    #az ablak aljáról pattanjon vissza
    if labda.ycor() <-288:
        labda.sety(-288)
        labda.valtozasY *=-1 # a valtozo ertekének előjele megváltozik

    #FONTOS HOGY AZONOS POZICIOBAN KEZDOJON AZ IF, MERT CSAK ÍGY VANNAK AZONOS SZINTEN A PROGRAMBAN

    #LABDA VÍZSZINTES  MOZGÁSÁNAK LKEZELÉSE
    #az ablak jobb oldalát eléri, akkor vége a játék , középre áll vissza 
    if labda.xcor() > 388: #400 lenne a jó de a labdának van kiterjedése ezért kisebb értéket adunk meg
        labda.goto(0,0)
        labda.valtozasX *=-1 # a valtozo ertekének előjele megváltozik, hogy a masik utő irányába menjen a labda
        #pontszámolás és kiírása újból
        bal_pontszam +=1
        pontszam.clear()
        pontszam.write(f"Jobb játékos:{jobb_pontszam} Bal játékos: {bal_pontszam}", align="center",font=("curier",23,"normal"))
    #az ablak bal oldalát eléri, akkor vége a játék , középre áll vissza , 
    if labda.xcor() < -388: 
        labda.goto(0,0)
        labda.valtozasX *=-1 # a valtozo ertekének előjele megváltozik, hogy a masik utő irányába menjen a labda
        #pontszámolás és kiírása újból
        jobb_pontszam +=1
        pontszam.clear()
        pontszam.write(f"Jobb játékos:{jobb_pontszam} Bal játékos: {bal_pontszam}", align="center",font=("curier",23,"normal"))

    #A LABDA ÉS AZ UTO ERINTÉSENEK LEKEZELÉSE
    #A JOBB OLDALI UTŐ, kiterjedése miatt
    # ha az utoX-20 kordináta elérese esetén megfordul a labda , azaz elértem , de biztonság miatt vizsgálom az utő közepét is 
    # ha az utoY-40 és az utoY+40 koordináta(az ütő függőleges kiterjedése) elérése esetén megfordul , mert elértem  a labdát 
    # (egyébként majd középre)
    if jobb_uto.xcor()-20 < labda.xcor() < jobb_uto.xcor() and jobb_uto.ycor()-40 < labda.ycor() < jobb_uto.ycor()+40:
        labda.setx(jobb_uto.xcor()-20)
        labda.valtozasX *= -1
       
    #A BAL OLDALI UTŐ, kiterjedése miatt
    # ha az utoX+20 kordináta elérese esetén megfordul a labda , azaz elértem a bal ütóvel, de biztonság miatt vizsgálom az utő közepét is 
    # ha az utoY-40 és az utoY+40 koordináta(az ütő függőleges kiterjedése) elérése esetén megfordul , mert elértem  a labdát 
    # (egyébként majd középre)
    if bal_uto.xcor()+20 > labda.xcor() > bal_uto.xcor() and bal_uto.ycor()-40 < labda.ycor() < bal_uto.ycor()+40:
        labda.setx(bal_uto.xcor()+20)
        labda.valtozasX *= -1

    

       

