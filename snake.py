
import turtle
import random

"""
1. If the snake is moving left, and you press right, it gets treated
as a self-collision, and with other directions. Fix it

2. Make a counter for how many foods you ate AND display it on the
turtle screen

3. Make a visible border, and make SURE that the food created is inside
the border. Remember to change the boundaries so that if you go outside the border
then the game will exit
Yalla good luck
"""

border=turtle.clone()

turtle.tracer(1,0)
SIZE_X=900
SIZE_Y=600
border.hideturtle()
border.penup()
border.goto(-400,-250)
border.pendown()
border.goto(-400,250)
border.goto(400,250)
border.goto(400,-250)
border.goto(-400,-250)


turtle.setup(SIZE_X,SIZE_Y)

turtle.penup()
SQUARE_SIZE=20
START_LENGTH=2
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

turtle.register_shape("wonder_woman.gif")
snake = turtle.clone()
snake.shape("wonder_woman.gif")


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

# food image setup + object
turtle.register_shape("jeff.gif") #Add trash picture
food = turtle.clone()
food.shape("jeff.gif")



direction = UP
def up():
    global direction
    if direction != DOWN:
        direction=UP 
        print("You pressed the up key!")

def left():
    global direction 
    if direction != RIGHT:
        direction=LEFT 
        print("You pressed the left key!")


def right():
    global direction
    if direction != LEFT:
        direction=RIGHT
        print("You pressed the right key!")


def down():
    global direction
    if direction != UP:
        direction=DOWN
         
        print("You pressed the left key!")

##on key shelf
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(up, UP_ARROW)
turtle.listen()
score=turtle.clone()
score.penup()
score.goto(300,250)
score1=0
########################################################################################################################
def write(score1):
    score.clear()
    score.write("Jeff count:" +
                str(score1) , font=("Arial", 20, "normal"))
########################################################################################################################

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(800/2/SQUARE_SIZE)+1
    max_x=int(800/2/SQUARE_SIZE)-1
    min_y=-int(500/2/SQUARE_SIZE)+1
    max_y=int(500/2/SQUARE_SIZE)-1
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    
    food.goto(food_x,food_y)
    
    newest_food_pos=(food_x,food_y)
    food_pos.append(newest_food_pos)
    
    food_ID=food.stamp()
    food_stamps.append(food_ID)


########################################################################################################################


def move_snake():
    global direction ,score1
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

    # make head
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    
    ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos
    #If snake is on top of food item
    
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) 
        food.clearstamp(food_stamps[food_ind])
        #stamp
        food_pos.pop(food_ind) 
        food_stamps.pop(food_ind) 
        print('You have eaten the food!')
        score1=score1+1
        write(score1)
        make_food()

    else:
        # deletes the tail        
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    
    if my_pos in pos_list[:-1]:
        print("you ate yourself!!")
        quit()
        
##################################################################################

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
make_food()
move_snake()

##FOOD


###Locations of food
##food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
##food_stamps = []
##
##
##for this_food_pos in food_pos :
##    food.goto(this_food_pos)
##    food_ID = food.stamp()
##    food_stamps.append(food_ID)


##FOOD (END)




turtle.mainloop()





#list_name[:-1]
