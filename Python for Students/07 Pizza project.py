import turtle

# Python úzus - konštanty sú UPPER CASE !!!
BACKGROUND_COLOR = "#9EC388"
CRUST_COLOR = "#ECA84F"
SAUCE_COLOR = "#AD0509"
CHEESE_COLOR = "#FBC70F"
PEPPERONI_LOCATIONS = [
    [-70, 105],
    [-85, 175],
    [-25, 50],
    [-15, 100],
    [-25, 150],
    [-30, 205],
    [15, 50],
    [20, 120],
    [20, 200],
    [60, 156],
    [71, 215],
    [80, 90],
    [95, 150]
]

# screen
screen = turtle.Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.title("kreslime")
# screen.delay(1) # moje, ale asi nefunguje

# pen
my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.speed('fast')
# my_turtle.shape("circle")

def draw_circle(radius, line_color, fill_color):
    my_turtle.color(line_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()

def move_turtle(x,y):
    my_turtle.up() # = penup
    my_turtle.goto(x,y)
    my_turtle.down() # = pendown

my_offset = -100 # ADDED FOR CENTERING 
move_turtle(0,my_offset) # goto down by my_offset

# základ
draw_circle(150, CRUST_COLOR, CRUST_COLOR)
move_turtle(0, my_offset + 25)
draw_circle(125, SAUCE_COLOR, CHEESE_COLOR)

# čerešničky
for location in PEPPERONI_LOCATIONS:
    move_turtle(location[0], my_offset + location[1])
    draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)

# hviezda, slicing our pizza
move_turtle(0, my_offset + 150)
my_turtle.color(BACKGROUND_COLOR)

for i in range(8): 
    my_turtle.forward(150)
    my_turtle.backward(150)
    my_turtle.left(45)

turtle.done() # must be!
