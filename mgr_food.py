import turtle


def food_mgt():
    # food
    food = turtle.Turtle()
    food.speed(0)
    food.shape('square')
    food.color('orange')
    food.penup()
    food.goto(0, 100)

    def fn_goto(x, y):
        food.goto(x, y)

    return food, fn_goto
