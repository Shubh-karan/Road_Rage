from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.color("black")
        self.shape("turtle")
        self.go_back()

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        new_x = self.xcor()
        self.goto(new_x,new_y)

    def go_back(self):
        self.goto(STARTING_POSITION)

    def at_Finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            False

    
        

