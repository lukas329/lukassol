import turtle
pero= turtle.Turtle()
tabula= turtle.Screen()
pero.speed(0)

n1=int(tabula.numinput("číslo n1", "Využijeme Eulerov poznatok e = 1 + 1/1! + 1/2! + 1/3! + ...1/n!. Zadaj ľubovoľné prirodzené číslo:"))
n2=int(tabula.numinput("číslo n2", "Zadaj ľubovoľné prirodzené číslo väčšie ako predchádzajúce:"))
n3=int(tabula.numinput("číslo n3", "Zadaj ľubovoľné prirodzené číslo väčšie ako predchádzajúce:"))
n4=int(tabula.numinput("číslo n4", "Zadaj ľubovoľné prirodzené číslo väčšie ako predchádzajúce:"))
n5=int(tabula.numinput("číslo n5", "Zadaj ľubovoľné prirodzené číslo väčšie ako predchádzajúce:"))

def fakt(n):
    fakt = 1
    for i in range(2, n+1):
        fakt = fakt * i
    return fakt

def vypocet(n):
    pero.write(n, font=25)
    pero.penup()
    pero.forward(300)
    pero.pendown()
    euler=1
    for i in range (1, n+1):
        euler=euler + 1/fakt(i)
    pero.write(euler, font=25)

def obdlznik():
    pero.forward(500)
    pero.left(90)
    pero.forward(40)
    pero.left(90)
    pero.forward(500)
    pero.left(90)
    pero.forward(40)

def tabulka():
    obdlznik()
    for i in range (4):
        pero.forward(40)
        pero.left(90)
        obdlznik()

pero.pencolor("Black")
pero.penup()
pero.goto(-250, 150)
pero.pendown()
vypocet(n1)

pero.penup()
pero.goto(-250, 110)
pero.pendown()
vypocet(n2)

pero.penup()
pero.goto(-250, 70)
pero.pendown()
vypocet(n3)

pero.penup()
pero.goto(-250, 30)
pero.pendown()
vypocet(n4)

pero.penup()
pero.goto(-250, -10)
pero.pendown()
vypocet(n5)

pero.penup()
pero.goto(-260, 150)
pero.pendown()
tabulka()

pero.penup()
pero.goto(-50,-10)
pero.pendown()
pero.left(180)
pero.forward(240)

pero.penup()
pero.goto(-260, 190)
pero.pendown()
pero.right(90)
pero.forward(500)
pero.left(90)
pero.forward(40)
pero.left(90)
pero.forward(500)
pero.left(90)
pero.forward(40)

pero.penup()
pero.goto(-250, 190)
pero.pendown()
pero.write("n=", font=50)

pero.penup()
pero.goto(-40, 190)
pero.pendown()
pero.write("Výsledok blížiaci sa k Eulerovmu číslu:", font=50)

pero.penup()
pero.goto(0, -200)
pero.penup()
pero.write("e= 2.718 281 828 459 045 235 360 287...", font=50)

pero.hideturtle()
tabula.mainloop()

