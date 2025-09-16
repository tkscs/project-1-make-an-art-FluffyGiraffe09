import turtle
turtle.speed(10)
number_of_sides = 100

# head:
def draw_circle(move):  
    for i in range(number_of_sides):
            turtle.forward(move)
            turtle.right(360 / number_of_sides)
draw_circle(9)

for i in range(number_of_sides//6):
    turtle.forward(9)
    turtle.right(360 / (number_of_sides))

# ears:
turtle.left(135)
for i in range(number_of_sides//10):
    turtle.forward(10)
    turtle.left(360 / (number_of_sides))
turtle.left(84)
for i in range(number_of_sides//12):
    turtle.forward(10)
    turtle.left(360 / (number_of_sides))
turtle.up()
turtle.right(49)
turtle.forward(75)
turtle.down()
turtle.right(50)
for i in range(number_of_sides//12):
    turtle.forward(10)
    turtle.left(360 / (number_of_sides))
turtle.left(87)
for i in range(number_of_sides//10):
    turtle.forward(10)
    turtle.left(360 / (number_of_sides))
turtle.up()
turtle.left(50)
turtle.forward(80)
turtle.down()

# eyes:
draw_circle(3)
turtle.up()
turtle.left(33)
turtle.forward(105)
turtle.down()
draw_circle(3)
turtle.up()
turtle.right(123)
turtle.forward(115)
turtle.down()

# nose and mouth:
for i in range(3):
        turtle.forward(15)
        turtle.right(360 / 3)
turtle.forward(15)
turtle.left(30)
turtle.forward(10)
turtle.right(30)
turtle.forward(15)
turtle.left(360 / 3)
turtle.up()
turtle.forward(15)
turtle.down()
turtle.left(360 / 3)
turtle.forward(15)
turtle.up()
turtle.left(60)
turtle.forward(20)
turtle.down()

# whiskers(left):
def draw_whiskers(angle, number):
    for i in range(number_of_sides//5):
        turtle.forward(9)
        turtle.left(angle / number_of_sides)
    turtle.right(number)
    for i in range(number_of_sides//5):
        turtle.forward(9)
        turtle.right(angle / number_of_sides)

draw_whiskers(300, 183)
turtle.right(183)
draw_whiskers(200, 182)
turtle.right(183)
draw_whiskers(100, 181)

turtle.up()
turtle.left(13)
turtle.forward(40)
turtle.down()

# whiskers(right):
def draw_whiskers(angle, number):
    for i in range(number_of_sides//5):
        turtle.forward(9)
        turtle.right(angle / number_of_sides)
    turtle.left(number)
    for i in range(number_of_sides//5):
        turtle.forward(9)
        turtle.left(angle / number_of_sides)

draw_whiskers(300, 183)
turtle.left(183)
draw_whiskers(200, 182)
turtle.left(183)
draw_whiskers(100, 181)
turtle.left(183)





# crazy eyes:
# def draw_circle(number_of_sides):
#     for i in range(number_of_sides):
#         turtle.forward(2)
#         turtle.right(90 / number_of_sides)

# for number_of_sides in range(1, 15):
#     draw_circle(number_of_sides)


# def draw_polygon(number_of_sides):
#     for i in range(number_of_sides):
#         turtle.forward(100)
#         turtle.right(360 / number_of_sides)

# for number_of_sides in range(3, 8):
#     draw_polygon(number_of_sides)