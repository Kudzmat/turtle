import turtle

kirby = turtle.Turtle()
screen = turtle.Screen().bgcolor('black')
kirby.speed(0)
for i in range(360):
    kirby.color('yellow')
    kirby.left(1)
    kirby.fd(1)
    for j in range(2):
        kirby.left(2)
        kirby.circle(100)
