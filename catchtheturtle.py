import turtle , time , random
from random import randint

#Ekran kodları
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("lightblue")
turtle_screen.title("Catch The Turtle ")

FONT = ('Arial', 20, 'normal')

#Skor kodları
skor=turtle.Turtle()
skor.hideturtle()
skor.penup()
skor.goto(0,250)
skor.write("Skorunuz :0", align="center", font=FONT)

#skor degisimi
score=0
def score_guncelle():
     skor.clear()
     skor.write(f"score: {score}", align="center", font=(FONT))

#Random Turtle Oluşturma

random_turtle=turtle.Turtle("turtle")
random_turtle.color("green")
random_turtle.shapesize(2,2)
random_turtle.penup()

score = 0
def make_random_turtle(x,y):
    global score
    xekseni=randint(-200,200)
    yekseni=randint(-200,200)
    random_turtle.goto(xekseni,yekseni)
    score = score + 1
    score_guncelle()

random_turtle.onclick(make_random_turtle)

#Timer
from turtle import Screen, Turtle
def countdown(time):
    screen.onclick(None)
    turtle.clear()
    if time > 0:
        turtle.write("Kalan Süre: " + str(time), align='center', font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        turtle.write("Süreniz Doldu!", align='center', font=FONT)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()
turtle.goto(0,290)
turtle.write("Başlamak için Ekrana Tıklayınız!", align='center', font=FONT)
screen = Screen()
screen.onclick(lambda x, y: countdown(30))

screen.mainloop()



