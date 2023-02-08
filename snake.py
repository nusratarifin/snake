import turtle
import time
import random
from turtle import Turtle

from mgr_food import food_mgt

delay = 0.1

# score
score = 0
high_score = 0
food = food_mgt()
# screen
wn = turtle.Screen()
wn.title('Snake Game by Jui')
wn.bgcolor("light green")
wn.setup(width=600, height=600)
wn.tracer(0)

# head
head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('brown')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# food
# food = turtle.Turtle()
# food.speed(0)
# food.shape('square')
# food.color('orange')
# food.penup()
# food.goto(0, 100)

# body
segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('circle')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write('Score:0, High Score:0', align='center', font=('Courier New', 24, 'normal'))


def go_up():
    if head.direction != 'down':
        head.direction = 'up'


def go_down():
    if head.direction != 'up':
        head.direction = 'down'


def go_left():
    if head.direction != 'right':
        head.direction = 'left'


def go_right():
    if head.direction != 'left':
        head.direction = 'right'


def move():
    if head.direction == 'up':
        yo = head. ycor()
        head.sety(yo + 20)

    if head.direction == 'down':
        yo = head. ycor()
        head.sety(yo - 20)

    if head.direction == 'left':
        xo = head. xcor()
        head.setx(xo - 20)

    if head.direction == 'right':
        xo = head. xcor()
        head.setx(xo + 20)


wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')

# main game loop
while True:
    wn.update()
    # collision with boarder
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        # hide the segment
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segments list
        segments.clear()

        # reset the score
        score = 0

        # reset the delay
        delay = 0.1
        pen.clear()
        pen.write('Score: {} High Score {}'.format(score,high_score), align='center', font=('Courier New', 24, 'normal'))

    # collision with food
    if head.distance(food) < 20:
        # move the food random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('gray')
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001

        # increase the score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write('Score: {} High Score {}'.format(score,high_score), align='center', font=('Courier New', 24, 'normal'))

    # move the end segments first to the reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    # check for head collision with the body segments
    segment: Turtle
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            # hide the segment
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segments list
            segments.clear()

            # update score
            score = 0

            # reset the delay
            delay = 0.1

            # update the score display
            pen.clear()
            pen.write('Score: {} High Score {}'.format(score,high_score), align='center', font=('Courier New', 24, 'normal'))

    time.sleep(delay)

wn.mainloop()
