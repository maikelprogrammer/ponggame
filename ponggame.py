from turtle import Screen,Turtle
import time

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("THE FAMOUS PONG GAME")
screen.tracer(0)

class Paddle(Turtle):

    def __init__(self,positions):
        super().__init__()
        self.shape("square")
        self.color("deepSkyBlue")
        self.penup()
        self.shapesize(5,1)
        self.goto(positions)

    def go_up(self):
        new_y=self.ycor()+15
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() -15
        self.goto(self.xcor(), new_y)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("IndianRed")
        self.penup()
        self.goto(0,0)
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y = self.ycor() +self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move*=-1

    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("courier", 30, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("courier", 30, "normal"))


    def l_point(self):
        self.l_score+=1
        self.clear()
        self.update_score()


    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()

r_paddle=Paddle((360,0))
l_paddle=Paddle((-360,0))
ball=Ball()
score=Score()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #detect collision with y.cor() and bounce
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with paddle and bounce
    if ball.distance(r_paddle)<60 and ball.xcor()>320 or ball.distance(l_paddle)<60 and ball.xcor()<-320:
        ball.bounce_x()

    #detect when r_paddle misses
    if ball.xcor()>380:
        score.l_point()
        ball.reset_position()

    #detect when l_paddle misses
    if ball.xcor()<-380:
        score.r_point()
        ball.reset_position()

screen.exitonclick()

