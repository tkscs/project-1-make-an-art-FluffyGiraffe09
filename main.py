import turtle

turtle.tracer(0, 0)

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
turtle.goto(-30,0)
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
y=3
x=2
# this circle variable (x) can take values 0.5 to 3-->this variable changes the size of the inner eye pupil, if you make this value the same as y, then it wont have an inner circle, if it is different than the value of y, it has an inner circle (the smaller you make the # the crazier the cat looks)
if x == y:
    draw_circle(y)
elif x < y:
    draw_circle(y)
    turtle.up()
    turtle.goto(-45, -93)
    turtle.down()
    draw_circle(x)
turtle.up()
turtle.left(33)
turtle.goto(65, -85)
turtle.down()
if x == y:
    draw_circle(x)
elif x < y:
    draw_circle(y)
    turtle.up()
    turtle.goto(65, -93)
    turtle.down()
    draw_circle(x)


turtle.up()
turtle.goto(9, -183)
turtle.right(123)
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
def draw_whiskers_left(angle, number):
    for i in range(number_of_sides//5):
        turtle.forward(9)
        turtle.left(angle / number_of_sides)
    turtle.right(number)
    for i in range(number_of_sides//5):
        turtle.forward(9)
        turtle.right(angle / number_of_sides)

for whisker_number_left in range(3):
    draw_whiskers_left(300+whisker_number_left*(-100), 183+whisker_number_left*(-1))
    turtle.right(183)




turtle.up()
turtle.left(183)
turtle.left(13)
turtle.forward(40)
turtle.down()

# whiskers(right):
def draw_whiskers_right(angle, number):
    for i in range(number_of_sides//5):
        turtle.forward(9)
        turtle.right(angle / number_of_sides)
    turtle.left(number)
    for i in range(number_of_sides//5):
        turtle.forward(9)
        turtle.left(angle / number_of_sides)

for whisker_number_right in range(3):
    draw_whiskers_right(300+whisker_number_right*(-100), 183+whisker_number_right*(-1))
    turtle.left(183)


# heart:
turtle.up()
turtle.goto(10, 30)
turtle.down()
angle=35
# if you change what the angle equals, it changes the tilt of the heart, it can take a range of values from 20 to 80 (it can have a larger range, but it will look pretty weird because the heart will be pretty much side ways)
turtle.left(angle)
turtle.forward(35)
number_of_semi_sides = 50
def draw_semicircle(move):
    for i in range(number_of_semi_sides//2):
            turtle.forward(move)
            turtle.left(360 / number_of_semi_sides)
draw_semicircle(2)
turtle.right(100)
draw_semicircle(2)
turtle.goto(10, 30)
turtle.up()

# blush
# turtle.goto(-115,-185)
# turtle.down()
# turtle.left(70)
# angle=35
# turtle.left(angle)
# turtle.forward(15)
# number_of_semi_sides = 20
# def draw_semicircle(move):
#     for i in range(number_of_semi_sides//2):
#             turtle.forward(move)
#             turtle.left(360 / number_of_semi_sides)
# draw_semicircle(2)
# turtle.right(100)
# draw_semicircle(2)
# turtle.goto(-115,-185)
# turtle.up
# turtle.goto(0,0)


turtle.update()
turtle.exitonclick()
