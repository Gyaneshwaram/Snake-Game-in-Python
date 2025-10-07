import turtle
import random
import time

# Initial settings
delay = 0.1
score = 0
high_score = 0
bodies = []

# Create screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("light blue")
screen.setup(width=600, height=600)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor("blue")
food.penup()
food.goto(100, 0)

# Scoreboard
sb = turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-290, 270)
sb.write("Score: 0    | Highest score: 0", font=("Arial", 14, "bold"))

# Movement functions
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_stop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_stop, "space")

# Main game loop
while True:
    screen.update()

    # Border collision logic (wrap around)
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add new body segment
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("red")
        body.penup()
        bodies.append(body)

        # Update score and delay
        score += 100
        delay = max(0.05, delay - 0.001)  # Cap the minimum delay
        if score > high_score:
            high_score = score

        # Update scoreboard
        sb.clear()
        sb.write(f"Score: {score}    | Highest score: {high_score}", font=("Arial", 14, "bold"))

    # Move the body segments
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with own body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for body in bodies:
                body.hideturtle()
            bodies.clear()

            score = 0
            delay = 0.1
            sb.clear()
            sb.write(f"Score: {score}    | Highest score: {high_score}", font=("Arial", 14, "bold"))

    time.sleep(delay)

# Keep the window open (not reached due to infinite loop)
screen.mainloop()
