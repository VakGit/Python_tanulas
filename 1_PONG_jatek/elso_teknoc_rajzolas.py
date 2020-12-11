#beolvasása egy meglévő osztálynak 
import turtle

#ABLAK létrehozása

ablak = turtle.Screen()
#ablak mérete
ablak.setup(width=800, height=600)
#ablak háttere 
ablak.bgcolor("pink")
ablak.title("TEKNOC_RAJZ")

#kikapcsolja a teknos objektum animálását megjelenését kirajzolását az ablakon belül , egy nem negativ szammal
#ablak.tracer(0)

#egy teknőssel rajzolunk 
#objektum letrehozsa
petiteknos=turtle.Turtle()

#az alakjat meghatarozzuk
petiteknos.shape("turtle")

#Megváltoztatjuk a toll alakját
#petiteknos.shape("square")

#a méretét állítjuk
petiteknos.shapesize(stretch_wid=5, stretch_len=5)
#a színét
petiteknos.color("yellow")

#toll le, a rajzolashoz
petiteknos.pendown()

#írása egy szöveg, az objektum alapszinét örökli lsd. obj.color("green")
#a szöveg szinét a toll szinének módosításával állithatjuk
petiteknos.pencolor("green")
petiteknos.write("Kezdet",align="center",font=("curier",45,"normal"))

#a tollat felemeljukm nem rajzol semmit csak az alak mozog 
#petiteknos.penup()

# a toll szinének ismételt megváltoztatása  
petiteknos.pencolor("blue")

#a toll sebessege
petiteknos.speed(1)

#A TOLLAL VALO IRAS forward() mozog és ir ha lent van a toll, right() és left() szöggel való elfordulás 
#toll iranya és irasanak hossza
petiteknos.forward(200)
petiteknos.right(90)
petiteknos.forward(200)
petiteknos.right(90)
petiteknos.forward(200)
petiteknos.right(90)
petiteknos.forward(200)
petiteknos.right(90)

# a toll szinének visszaállítása
petiteknos.pencolor("black")

"""
#Kilépes 0
#ne szaladjon el a kep , vegtelen ciklus egy módja hogy a progrm ne zárjon be , nem igazan jo csak KILL-ezni lehet (kiloni)
while True:
    pass
"""


#MÉG HÁROM KILÉPÉSI MÓD
"""
#I:
#AZ ABLAKBOL NORMAL MODON VALO KILEPESHEZ EZ TÖBBSZÖR RAJZOL ÉS KÖRBE - KÖRBE MOZGAST IS ANIMAL 
#  - EGY CIKLUS KELL
#  - EGY BILLENTYUZET FIGYELES ES MINDEN OKÉ :J

#Az ablakban a Billentyúzet figyelés bakapcsolasa Alt-F4 és egérrel ki lehet lépni
ablak.listen()

#és a ciklus
while True:
    petiteknos.pencolor("green")
    
    petiteknos.write("Kezdet",align="center",font=("curier",45,"normal"))
    
    petiteknos.pencolor("blue")
    
    petiteknos.speed(1)

    petiteknos.forward(200)
    petiteknos.right(90)
    petiteknos.forward(200)
    petiteknos.right(90)
    petiteknos.forward(200)
    petiteknos.right(90)
    petiteknos.forward(200)
    petiteknos.right(90)

    petiteknos.pencolor("black")
"""


#II.
#billentyuzet figyelésének bekapcsolás és egy ciklus, egy ures utasitassal  ALT-F4 és X egérrel él , Nem mozog tovabb a teknos !!!


#Billentyúzet figyelés bakapcsolasa Alt-F4 és egérrel ki lehet lépni
ablak.listen()

#ures ciklus
while True:
    petiteknos.write("")#egy üres utasitas kell ertekadas nem eleg pld. semmi=true vagy pass hiba , de miért ? MAJD kiderul :)
