import turtle

# Setup screen
wn = turtle.Screen()
wn.title("Pong by CGGamer")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle class
class Paddle(turtle.Turtle):
    def __init__(self, position, size):
        super().__init__()
        self.position = position
        self.size = size
        self.speed(0)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=size)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        y = self.ycor()
        y += 20
        if y < 250:  # Limiting paddle movement to stay within screen bounds
            self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        if y > -240:  # Limiting paddle movement to stay within screen bounds
            self.sety(y)

# Ball class
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 0.15  # Ball movement speed along x-axis
        self.dy = 0.15  # Ball movement speed along y-axis

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        # Border collision
        if self.ycor() > 290 or self.ycor() < -290:
            self.dy *= -1

        if self.xcor() > 390 or self.xcor() < -390:
            self.goto(0, 0)
            self.dx *= -1

# Create paddles
paddle_a = Paddle((-350, 0), 1)
paddle_b = Paddle((350, 0), 1)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a.move_up, "w")
wn.onkeypress(paddle_a.move_down, "s")
wn.onkeypress(paddle_b.move_up, "Up")
wn.onkeypress(paddle_b.move_down, "Down")

# Create ball
ball = Ball()

# Main game loop
while True:
    wn.update()
    ball.move()

