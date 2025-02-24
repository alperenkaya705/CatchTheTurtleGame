#catch_the_turtle_game
import turtle, time, random
from random import randint

# Ekran kodları
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("lightblue")
turtle_screen.title("Catch The Turtle ")

FONT = ('Arial', 20, 'normal')

game_over = False
score = 0

def score_guncelle():
    skor.clear()
    skor.goto(0, 250)
    if not game_over:
        skor.write(f"Skorunuz: {score}", align="center", font=FONT)
    else:
        skor.goto(0, 0)
        skor.write(f"Skorunuz: {score}\nYeniden başlamak için tıklayın!", align="center", font=FONT)

def make_random_turtle(x, y):
    global score, game_over
    if not game_over:
        xekseni = randint(-200, 200)
        yekseni = randint(-200, 200)
        random_turtle.goto(xekseni, yekseni)
        score += 1
        score_guncelle()

def countdown(time):
    global game_over
    screen.onclick(None)
    timer.clear()
    if time > 0:
        timer.write(f"Kalan Süre: {time}", align='center', font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        random_turtle.hideturtle()
        score_guncelle()
        screen.onclick(restart_game)

def restart_game(x, y):
    global score, game_over
    score = 0
    game_over = False
    random_turtle.showturtle()
    score_guncelle()
    countdown(30)

# Skor gösterme
skor = turtle.Turtle()
skor.hideturtle()
skor.penup()
skor.goto(0, 250)
skor.write("Skorunuz :0", align="center", font=FONT)

# Rastgele Turtle oluşturma
random_turtle = turtle.Turtle("turtle")
random_turtle.color("green")
random_turtle.shapesize(2, 2)
random_turtle.penup()
random_turtle.onclick(make_random_turtle)

# Timer
screen = turtle.Screen()
timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(0, 290)
timer.write("Başlamak için Ekrana Tıklayınız!", align='center', font=FONT)
screen.onclick(lambda x, y: countdown(30))

screen.mainloop()
