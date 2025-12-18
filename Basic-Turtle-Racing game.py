import random
import turtle
from turtle import Turtle,Screen

screen = Screen()
screen.setup(height=500,width=500)
turtle.colormode(255)

color_list = ["azure","coral","cyan","brown","blue","gold","green"]

y_cor = [180,120,60,0,-60,-120,-180]

user_bet = screen.textinput(title="Place your bet",prompt="Which turtle will win? Enter a color :-\nYour options are (azure,coral,cyan,brown,blue,gold,green) ")
user_option = ('azure','coral','cyan','brown','blue','gold','green')

race_is_on = True
if user_bet:
    race_is_on = True
elif any(user_option) in user_bet:
    race_is_on = True
else:
    race_is_on = False

po_list = []
for turtle_no in range(0,7):
    po = Turtle(shape="turtle")
    po.color(color_list[turtle_no])
    po.penup()
    po.goto(x=-230, y=y_cor[turtle_no])
    po_list.append(po)
while race_is_on:
    for po1 in po_list:
        po1.speed(0)
        po1.forward(random.randrange(0,10))
        if po1.xcor() > 240:
            race_is_on = False
            turtle_color = list(po1.color())
            # or  turtle_color = po1.pencolor()
            if user_bet == turtle_color[0]:
                print("yayy!! , you won")
            else:
                print(f"Opps! , {turtle_color[0]} turtle is the winner\nBetter luck next time")

screen.exitonclick()
