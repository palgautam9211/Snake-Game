import turtle
import random
import time
bodies=[]
delay=0.1
score=0
highest_score=0

s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("Grey")
s.setup(width=600,height=600)

#creating snake head
head=turtle.Turtle()
head.shape("square")
head.color("red")
head.speed(0)
head.fillcolor("red")
head.penup()
head.goto(0,0)
head.direction="stop"

#create a food
food=turtle.Turtle()
food.shape("circle")
food.color("yellow")
food.fillcolor("green")
food.speed(0)
food.ht()
food.penup()
food.goto(0,200)
food.showturtle()


#score board
score_board=turtle.Turtle()
score_board.shape("square")
score_board.fillcolor("black")
score_board.penup()
score_board.ht()
score_board.goto(-250,-250)
score_board.write("Score: 0  | Heighest score: 0")


def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movestop():
    head.direction="stop"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

#key handling
s.listen()
s.onkey(movedown,"Down")
s.onkey(moveup,"Up")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")



#main loop
while True:
    s.update()

    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)

    if head.distance(food)<20:
          x=random.randint(-290,290)
          y=random.randint(-290,290)
          food.goto(x,y)

          #increase length of snake
          body=turtle.Turtle()
          body.shape("square")
          body.speed(0)
          body.color("red")
          body.fillcolor("black")
          body.penup()
          bodies.append(body)

          score+=10
          delay-=0.001
          if score>highest_score:
              highest_score=score
          score_board.clear()
          score_board.write("Score: {} Highest score: {}".format(score,highest_score))
          
          
      #snake moving
    for index in range (len(bodies)-1,0,-1):
       x=bodies[index-1].xcor()
       y=bodies[index-1].ycor()
       bodies[index].goto(x,y)
    
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for body in bodies:
                body.ht()
            bodies.clear()
            score=0
            delay=0.1
            score_board.clear()
            score_board.write("Score: {} | Highest score: {}".format(score,highest_score))
    time.sleep(delay)    

s.mainloop()
