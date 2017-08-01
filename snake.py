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

##EDGE
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
##EDGE END

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
     #Update the snake drawing <- remember me later
    print("You pressed the up key!")
    #2. Make functions down(), left(), and right() that change
    #direction
    ####WRITE YOUR CODE HERE!!
 # Create listener for up key
turtle.listen()

def left():
    global direction 
    direction=LEFT 
     
    print("You pressed the left key!")

turtle.listen()

def right():
    global direction 
    direction=RIGHT
     
    print("You pressed the right key!")

turtle.listen()

def down():
    global direction 
    direction=DOWN
     
    print("You pressed the left key!")

##on key shelf
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(up, UP_ARROW)
turtle.listen()

########################################################################################################################

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
    ## position
    ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list

    ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list


########################################################################################################################


def move_snake():
    global direction
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    ##RIGHT/left
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")


    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")

        
    ##UP/down
    elif direction==UP:
        snake.goto(x_pos , y_pos+ SQUARE_SIZE)
        print("You moved up!")

        
    else:
        snake.goto(x_pos , y_pos- SQUARE_SIZE)
        print("You moved down!")
        
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    
    ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food

        #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print('You have eaten the food!')
        #HINT: This if statement may be useful for Part 8
        ...
        #Don't change the rest of the code in move_snake() function:
        #If you have included the timer so the snake moves
        #automatically, the function should finish as before with a
        #call to ontimer()
         #<--Last line of function

        #pop zeroth element in pos_list to get rid of last the last
        #piece of the tail
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)


##GAME OVER
    #RIGHT
    if new_x_pos >= RIGHT_EDGE:
        print('You hit the right edge! Game over!')
        quit()
#LEFT
    if new_x_pos <= LEFT_EDGE:
        print('You hit the left edge! Game over!')
        quit()

    #UP
    if new_y_pos >= UP_EDGE:
        print('You hit the upper edge! Game over!')
        quit()
    #DOWN
    if new_y_pos <= DOWN_EDGE:
        print('You hit the lower edge! Game over!')
        quit()
    turtle.ontimer(move_snake,TIME_STEP)
##GAME OVER(END)
move_snake()

##FOOD

turtle.register_shape("trash.gif") #Add trash picture


food = turtle.clone()
food.shape("trash.gif")
#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []


for this_food_pos in food_pos :
    food.goto(this_food_pos)
    food_ID = food.stamp()
    food_stamps.append(food_ID)


##FOOD (END)




turtle.mainloop()
