import turtle


def food_mgt():
    # food
    food = turtle.Turtle()
    food.speed(0)
    food.shape('square')
    food.color('orange')
    food.penup()
    food.goto(0, 100)

    return food
