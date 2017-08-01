import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup()
SQUARE_SIZE=20
START_LENGTH=8
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]


snake = turtle.clone()
snake.shape("square")


turtle.hideturtle()




for number in range(START_LENGTH):
    snake.stamp
    x_pos=snake.pos()[0] 
    y_pos=snake.pos()[1]

    x_pos=x_pos+SQUARE_SIZE
    my_pos=(x_pos,y_pos) 
    snake.goto(x_pos,y_pos)
    

    pos_list.append(my_pos)

    snake_stamp= snake.stamp()
    stamp_list.append(snake_stamp)
   ####MOVING AROND
UP_ARROW = "Up" #Make sure you pay attention to upper and lower

#case

LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many

#milliseconds

SPACEBAR = "space" # Careful, it's not supposed to be
#capitalized!
UP = 0
LEFT=1
DOWN=2
RIGHT=3




direction = UP
def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the up key!")
    #2. Make functions down(), left(), and right() that change
    #direction
    ####WRITE YOUR CODE HERE!!
 # Create listener for up key
turtle.listen()

def left():
    global direction 
    direction=LEFT 
    move_snake() 
    print("You pressed the left key!")

turtle.listen()

def right():
    global direction 
    direction=RIGHT
    move_snake() 
    print("You pressed the right key!")

turtle.listen()

def down():
    global direction 
    direction=DOWN
    move_snake() 
    print("You pressed the left key!")

##on key shelf
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(up, UP_ARROW)
turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    ##RIGHT/left
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
        snake.stamp()
        my_pos=snake.pos()
        pos_list.append(my_pos)
        new_stamp = snake.stamp()
        stamp_list.append(new_stamp)
        ######## SPECIAL PLACE - Remember it for Part 5
        #pop zeroth element in pos_list to get rid of last the last
        #piece of the tail
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)

    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
        snake.stamp()
        my_pos=snake.pos()
        pos_list.append(my_pos)
        new_stamp = snake.stamp()
        stamp_list.append(new_stamp)
        ######## SPECIAL PLACE - Remember it for Part 5
        #pop zeroth element in pos_list to get rid of last the last
        #piece of the tail
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        
    ##UP/down
    elif direction==UP:
        snake.goto(x_pos , y_pos+ SQUARE_SIZE)
        print("You moved up!")
        snake.stamp()
        my_pos=snake.pos()
        pos_list.append(my_pos)
        new_stamp = snake.stamp()
        stamp_list.append(new_stamp)
        ######## SPECIAL PLACE - Remember it for Part 5
        #pop zeroth element in pos_list to get rid of last the last
        #piece of the tail
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        
    elif direction==DOWN:
        snake.goto(x_pos , y_pos- SQUARE_SIZE)
        print("You moved down!")
        snake.stamp()
        my_pos=snake.pos()
        pos_list.append(my_pos)
        new_stamp = snake.stamp()
        stamp_list.append(new_stamp)
        ######## SPECIAL PLACE - Remember it for Part 5
        #pop zeroth element in pos_list to get rid of last the last
        #piece of the tail
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
