import random
import turtle
from turtle import Turtle,Screen
from turtle import colormode


import cv2, turtle, os

img_path = " " #absolute path of the image

step = 5     # Distance between dots (Increase this for more space)
dot_size = 5  # Size of the dot (Keep this smaller than 'step' for gaps)
# ------------------------


# Check if file exists before trying to resize
if not os.path.exists(img_path):
    print(f"FAILED: I cannot find '{img_path}'")
    print(f"I am currently looking in: {os.getcwd()}")
    print("Please move the image to this folder or use a full path.")
else:
    img = cv2.imread(img_path)
    img = cv2.resize(img, (200, 200), interpolation=cv2.INTER_AREA)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    s = turtle.Screen()
    s.setup(600,600)

    s.colormode(255)
    s.tracer(0) # remove this linen to see animation
    t = turtle.Turtle()
    t.penup()
    t.speed(10)

    for y, row in enumerate(img):
        for x, color in enumerate(row):
            # Multiply x and y by 'step' to create gaps
            # Centering logic: (x * step) - (total_width / 2) or you can tweak the values as per your needs
            t.goto(x * step - 300, 300 - y * step)
            t.color(color)
            t.dot(dot_size)
        s.update()

    print("Drawing Complete!")
    turtle.done()