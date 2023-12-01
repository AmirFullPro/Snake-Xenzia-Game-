import turtle
import time
import random

delay = 0.1

# Ochko
score = 0
high_score = 0

#Ekran funksyasi
wn = turtle.Screen()
wn.title("Snake Game by @deezy_002")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  #Ekran yabgiliklarini o'chirish

#Ilon o'sishi
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#ilon ovqati
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

#Qalam
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


#Funksiyalar
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Klavitura BIldirishi
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# O'yin boshi
while True:
    wn.update()

    # Chegara bilan tekshrish
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Sigmentlarni yashirish
        for segment in segments:
            segment.goto(1000, 1000)

        # Sigment listlarni tozalash
        segments.clear()

        #Restart berish
        score = 0

        # Delay Funksyasi
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Collisionni tekshirish
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #Sigment qo'shish
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Delay qisqartmasi ishlashi
        delay -= 0.001

        #Ochko oshirish
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        #Sigment birinchi chegaraga va aylanmaga qaytarish
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    #Ko'chirish
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    #Sigmentlarni tekshirish
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            #Malumotlarni yashirish
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list/ malumotlarni tozalash
            segments.clear()

            #Boshidan Boshlash
            score = 0

            #Delayni boshidan boshlash
            delay = 0.1

            #Ekranda ochkoni oshirish
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()