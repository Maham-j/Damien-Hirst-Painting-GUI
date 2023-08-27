# import colorgram

# colors = colorgram.extract('images.jpg',30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle
from turtle import Screen, Turtle
import random


screen = Screen()
turtle.colormode(255)
timmy = Turtle()

color_list = [(245, 241, 233), (227, 234, 242), (245, 234, 239), (233, 242, 236), (208, 158, 96), (234, 213, 101),
              (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55),
              (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36),
              (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167),
              (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]

timmy.hideturtle()
timmy.setheading(220)
timmy.penup()
timmy.forward(300)
timmy.setheading(0)
timmy.speed('fastest')

for _ in range(10):
    def draw_dots():
        for _ in range(10):
            timmy.dot(20, random.choice(color_list))
            timmy.penup()
            timmy.forward(50)
    draw_dots()


    def start_position(dots):
        timmy.setheading(90)
        timmy.pen()
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(360)


    start_position(draw_dots)


screen.exitonclick()
