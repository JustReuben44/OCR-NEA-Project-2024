import pygame
import pgzrun
import time
import random 
import os

class Button:
    def __init__(self, x, y, width, height, color, text, text_color, action):
        self.rect = Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.action = action

    def draw(self):
        screen.draw.filled_rect(self.rect, self.color)
        screen.draw.text(self.text, center=self.rect.center, color=self.text_color)

    def on_click(self, x, y):
        if self.rect.collidepoint(x, y):
            self.action()

def on_mouse_down(pos, button):
    for button in buttons:
        button.on_click(pos[0], pos[1])

def play_action():
    global game_complete
    print("Play button clicked")
    level_1()
    setup_actors()
    #triggers the first level

    game_complete = False


def HowToPlay_action():
    print("How to play button clicked")
    how_to_play()
    #triggers the how-to-play window


buttons = [
    Button(310, 225, 125, 30, (146, 13, 249), "Play", (48, 213, 200), play_action),
    Button(310, 325, 125, 30, (146, 13, 249), "How To Play", (48, 213, 200), HowToPlay_action)
]


def main_menu():
    global WIDTH, HEIGHT, game_title, GAMEMODE
    WIDTH = 750
    HEIGHT = 500
    # defines the width and height of the main menu screen
    game_title = Actor('title.png')
    game_title.pos = 375,100
    # sets the game title's position on screen (Top-Middle)
    GAMEMODE = "main menu"
    #gamemode is set to 0 to trigger the game title and buttons to be drawn on screen by the draw function

def how_to_play():
    global WIDTH, HEIGHT, GAMEMODE
    WIDTH = 750
    HEIGHT = 500
    # defines the width and height of the how to play screen
    GAMEMODE = "how to play"
    #level is set to 9 to trigger the screen to be cleared by the draw function
    
def draw_htp():
    screen.draw.text("Move the thief around the maze and collect all the coins to unlock the door to the next",(30,50), color= (200,200,200))
    screen.draw.text("level.",(350,75), color= (200,200,200))
    screen.draw.text("BE CAREFUL!",(315,100), color= (48, 213, 200))
    screen.draw.text("There are Security Guards scattered around the maze who will be chasing you.",(50,125), color= (200,200,200))
    screen.draw.text("If you are caught, the game is over…",(230,150), color= (48, 213, 200))
    screen.draw.text("Are You Ready?",(310,175), color =(200,200,200))
    screen.draw.text("Controls:",(25,225), color= (48, 213, 200))
    screen.draw.text("WASD or ARROW KEYS",(25,250), color= (200,200,200))
    screen.draw.text("Power-Ups (Once Per Game):",(25,275), color= (48, 213, 200))
    screen.draw.text("Dynamite – Destroys walls around the maze allowing you to move through places you",(25,300), color= (200,200,200))
    screen.draw.text("couldn’t.",(25,325), color= (200,200,200))
    screen.draw.text("Diamond – Grants you a speed boost.",(25,350), color= (200,200,200))
    screen.draw.text("Press “SPACE” To Return",(270,400), color= (48, 213, 200))
    box = Rect((265,395),(210,25))
    screen.draw.rect(box,(146, 13, 249))

def game_over_screen():
    global WIDTH, HEIGHT, game_over_title, caught_image, GAMEMODE
    WIDTH = 500
    HEIGHT = 400
    # defines the width and height of the main menu screen
    game_over_title = Actor('busted')
    game_over_title.pos = 260,150
    # sets the title's position on screen (Top-Middle)

    caught_image = Actor('caught')
    caught_image.pos = 90,320
    GAMEMODE = "game over"

def draw_game_over():
    screen.draw.text("You Were Caught!",(190,225), color= (200,200,200))
    screen.draw.text("Press “SPACE” To Try Again",(155,275), color= (200,200,200))

def game_won_screen():
    global WIDTH, HEIGHT, game_won_title, caught_image, GAMEMODE
    WIDTH = 500
    HEIGHT = 400
    # defines the width and height of the main menu screen
    game_won_title = Actor('level_cleared')
    game_won_title.pos = 260,150
    # sets the title's position on screen (Top-Middle)
    
    GAMEMODE = "game won"

    save_time()

def draw_game_won():
    screen.draw.text("Well done, you completed the level!",(120,225), color= (200,200,200))
    screen.draw.text("Time Taken:",(200,275), color= (200,200,200))
    screen.draw.text(str(real_time),(240,310), color= (200,200,200))
    screen.draw.text("Press “SPACE” To Start New Level!",(120,350), color= (200,200,200))

def game_complete_screen():
    global WIDTH, HEIGHT, game_complete_title, treasure_image, GAMEMODE
    WIDTH = 500
    HEIGHT = 400
    # defines the width and height of the main menu screen
    game_complete_title = Actor('congratulations')
    game_complete_title.pos = 260,150
    # sets the title's position on screen (Top-Middle)

    treasure_image = Actor('treasure_image')
    treasure_image.pos = 250,350
    
    GAMEMODE = "game complete"

    save_time()

def draw_game_complete():
    screen.draw.text("Time Taken:",(200,200), color= (200,200,200))
    screen.draw.text(str(real_time),(240,225), color= (200,200,200))
    screen.draw.text("You Have Beaten All Levels!",(150,250), color= (200,200,200))
    screen.draw.text("Press “SPACE” to Play Again and Beat Your Times",(75,275), color= (200,200,200))

def draw_usability_features():
    screen_end = WIDTH - 120
    screen.draw.text("Menu - (M)",(screen_end,10), color= (200,200,200), fontsize = 25)
    screen.draw.text("Restart - (R)",(screen_end,30), color= (200,200,200), fontsize = 25)
   
    

def update():
    global time1,real_time, game_over, game_won, game_complete
    time1 = time1 + 1
    if game_won == False and game_complete == False:
        real_time = time1//100
        

def draw_timer():
    screen_middle = (WIDTH/2, 30)
    screen.draw.text("Time: "+ str(real_time), midbottom = screen_middle , color= (200,200,200), fontsize = 30)


def save_time():
    if GAMEMODE == "game won" or GAMEMODE == "game complete":
        file_name = "level_" + str(LEVEL) + ".txt"
        with open(file_name, "a") as file:
            file.write(str(real_time) + "\n")
        #Saves user time to relevant file

def read_time():
    global scores
    scores = []
    if GAMEMODE == "play":
        file_name = "level_" + str(LEVEL) + ".txt"
        with open(file_name, "r") as file:
            for line in file:
                score = line.strip()
                if score:
                    scores.append(int(score))
                #Checks if the line is not empty
                    
        n = len(scores)
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, n):
                if scores[i - 1] > scores[i]:
                    scores[i - 1], scores[i] = scores[i], scores[i - 1]
                    swapped = True
                    
        #Sorts scores in ascending order

def draw_high_score():
    global scores
    read_time()

    if scores:
        high_score = scores[0]
    else:
        high_score = 0
        
    #Checks if there are scores available

    screen.draw.text("High Score: " + str(high_score), (25, 11), color=(200, 200, 200), fontsize=30)

def level_1():
    global WIDTH, HEIGHT, MAZE_HEIGHT, MAZE_WIDTH, MAZE_SIZE, MAZE, GAMEMODE, LEVEL
    MAZE_WIDTH = 12
    MAZE_HEIGHT = 8
    MAZE_SIZE = 50
    WIDTH = MAZE_WIDTH * MAZE_SIZE
    HEIGHT = MAZE_HEIGHT * MAZE_SIZE

    MAZE =[["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",],
           ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W",],
           ["W", "T", " ", " ", " ", " ", " ", " ", " ", " ", "C", "W",],
           ["W", " ", " ", " ", " ", " ", " ", " ", "A", " ", " ", "W",],
           ["W", " ", "W", "W", "W", "C", "W", "W", "W", "W", " ", "W",],
           ["W", " ", " ", "C", " ", " ", " ", " ", " ", " ", " ", "D",],
           ["W", " ", " ", " ", " ", "S", " ", " ", " ", "B", " ", "W",],
           ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W",],]

    GAMEMODE = "play"

    LEVEL = 1
    #Defines what level is currently being played

def level_2():
    global WIDTH, HEIGHT, MAZE_HEIGHT, MAZE_WIDTH, MAZE_SIZE, MAZE, GAMEMODE, LEVEL
    MAZE_WIDTH = 15
    MAZE_HEIGHT = 8
    MAZE_SIZE = 50
    WIDTH = MAZE_WIDTH * MAZE_SIZE
    HEIGHT = MAZE_HEIGHT * MAZE_SIZE

    MAZE = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "T", " ", "C", " ", " ", " ", " ", " ", " ", " ", "B", " ", " ", "W"],
            ["W", " ", "W", " ", "W", "W", "W", "W", " ", "W", "W", "W", "W", " ", "W"],
            ["W", " ", "W", "A", " ", " ", " ", " ", "S", " ", " ", "C", "W", " ", "W"],
            ["W", " ", "W", " ", "W", "W", "W", " ", "W", "W", "W", " ", "W", "C", "W"],
            ["W", " ", " ", " ", "W", " ", "C", " ", " ", " ", "W", " ", " ", " ", "W"],
            ["W", "W", "W", "W", "W", "D", "W", "W", "W", "W", "W", "W", "W", "W", "W"],]


    GAMEMODE = "play"

    LEVEL = 2
    #Defines what level is currently being played

def level_3():
    global WIDTH, HEIGHT, MAZE_HEIGHT, MAZE_WIDTH, MAZE_SIZE, MAZE, GAMEMODE, LEVEL
    MAZE_WIDTH = 15
    MAZE_HEIGHT = 10
    MAZE_SIZE = 50
    WIDTH = MAZE_WIDTH * MAZE_SIZE
    HEIGHT = MAZE_HEIGHT * MAZE_SIZE

    MAZE =[["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
           ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
           ["D", " ", " ", " ", " ", " ", "S", " ", " ", " ", "W", " ", " ", " ", "W"],
           ["W", " ", " ", " ", "C", " ", " ", " ", " ", " ", "W", " ", " ", "B", "W"],
           ["W", " ", "W", "W", "W", " ", " ", "W", "A", " ", "W", "S", " ", "W", "W"],
           ["W", " ", " ", " ", " ", " ", " ", "W", "W", "W", "W", "W", " ", "C", "W"],
           ["W", "C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
           ["W", "W", "W", "W", "W", " ", " ", "W", "W", "W", " ", "W", "W", " ", "W"],
           ["W", "T", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
           ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],]


    GAMEMODE = "play"

    LEVEL = 3
    #Defines what level is currently being played

def level_4():
    global WIDTH, HEIGHT, MAZE_HEIGHT, MAZE_WIDTH, MAZE_SIZE, MAZE, GAMEMODE, LEVEL
    MAZE_WIDTH = 15
    MAZE_HEIGHT = 10
    MAZE_SIZE = 50
    WIDTH = MAZE_WIDTH * MAZE_SIZE
    HEIGHT = MAZE_HEIGHT * MAZE_SIZE

    MAZE = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "D", "W", "W", "W"],
            ["W", "T", " ", " ", "W", " ", " ", "A", " ", " ", " ", " ", "W", "S", "W"],
            ["W", "W", "W", " ", "W", "C", "W", "W", "W", "W", " ", " ", "W", " ", "W"],
            ["W", "B", "W", " ", "W", " ", " ", " ", "S", "W", " ", " ", " ", " ", "W"],
            ["W", " ", "W", " ", " ", " ", "W", "W", " ", "W", "W", "W", "W", "C", "W"],
            ["W", " ", " ", " ", " ", " ", "W", " ", " ", "C", " ", " ", "W", " ", "W"],
            ["W", " ", "W", "W", "W", "W", "W", " ", "W", "W", "W", "W", "W", " ", "W"],
            ["W", "C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],]

    GAMEMODE = "play"

    LEVEL = 4
    #Defines what level is currently being played

def level_5():
    global WIDTH, HEIGHT, MAZE_HEIGHT, MAZE_WIDTH, MAZE_SIZE, MAZE, GAMEMODE, LEVEL
    MAZE_WIDTH = 15
    MAZE_HEIGHT = 11
    MAZE_SIZE = 50
    WIDTH = MAZE_WIDTH * MAZE_SIZE
    HEIGHT = MAZE_HEIGHT * MAZE_SIZE

    MAZE = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "T", " ", " ", " ", " ", " ", " ", "S", " ", " ", " ", " ", "C", "W"],
            ["W", " ", "W", "W", " ", "W", "W", "W", " ", "W", "W", "W", " ", "W", "W"],
            ["W", " ", "W", "W", " ", "W", "A", "W", "C", "W", " ", "W", " ", "W", "W"],
            ["W", " ", " ", "C ", " ", " ", " ", "W", " ", "W", " ","W", " ", " ", "D"],
            ["W", "W", "W", "W", " ", "W", "W", "W", " ", "W", " ", " ", " ", "W", "W"],
            ["W", " ", " ", " ", " ", "W", " ", " ", "B", " ", " ", "W", "S", " ", "W"],
            ["W", " ", "W", "W", "W", "W", " ", "W", "W", "W", " ", "W", " ", "W", "W"],
            ["W", " ", " ", " ", " ", "S", "C", "W", " ", " ", " ", " ", " ", "C", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],]

    GAMEMODE = "play"

    LEVEL = 5
    #Defines what level is currently being played


    
def draw_background():
    for y in range(len(MAZE)):
        for x in range(len(MAZE[y])):
            #Iterates through each row and column
            screen.blit("floor", screen_coords(y, x))
            if MAZE[y][x] == "0":
                screen.blit("black_ui", screen_coords(y, x))


def draw_boarder():
    for y in range(len(MAZE)):
        for x in range(len(MAZE[y])):
            #Iterates through each row and column
            if MAZE[y][x] == "W":   
                screen.blit("grey_wall", screen_coords(y, x))
            elif MAZE[y][x] == "D" and len(coins) > 0:
                    screen.blit("door", screen_coords(y, x))

def screen_coords(x, y):
    return y * MAZE_SIZE, x * MAZE_SIZE

def maze_coords(actor):
    return(round(actor.x/MAZE_SIZE), round(actor.y/MAZE_SIZE))

def setup_actors():
    global thief, THIEF_SPEED, security_guard, security_guards, coin, coins, powerup, powerups, time1, real_time
    time1 = 0
    real_time = 0
    THIEF_SPEED = 0.15
    security_guards = []
    coins = []
    powerups = []
    for y in range(len(MAZE)):
        for x in range(len(MAZE[y])):
            if MAZE[y][x] == "T":
                thief = Thief(x*MAZE_SIZE, y*MAZE_SIZE)
                #Initialise thief actor
            elif MAZE[y][x] == "S":
                security_guard = Enemy(x*MAZE_SIZE, y*MAZE_SIZE)
                #Initialise security guard actor
                security_guards.append(security_guard)
            elif MAZE[y][x] == "C":
                coin = Coin(x*MAZE_SIZE, y*MAZE_SIZE)
                #Initialise coin actor
                coins.append(coin)
            elif MAZE[y][x] == "A":
                powerup_type = "diamond"
                powerup = Powerup(powerup_type,x*MAZE_SIZE, y*MAZE_SIZE)
                #Initialise diamond actor
                powerups.append(powerup)
            elif MAZE[y][x] == "B":
                powerup_type = "dynamite"
                powerup = Powerup(powerup_type,x*MAZE_SIZE, y*MAZE_SIZE)
                #Initialise dynamite actor
                powerups.append(powerup)
                

    

class Thief(Actor):
    #Inherits Actor class
    def __init__(self, x, y):
        super().__init__("thief_right")
        self.anchor = ("left","top")
        self.pos = (x,y)
        #Sets thief position to the screen coordinates of the current maze position

    def move(self,dx, dy):
        global game_won, game_complete
        if game_over == True:
            return
        elif game_won == True:
            return
        elif game_complete == True:
            return

        if dx == -1:
            self.image = "thief_left"
        elif dx == 1:
            self.image = "thief_right"
        #Changes the thiefs image depending on what key the user pressed
        (current_x,current_y) = maze_coords(self)
        new_x = current_x + dx
        new_y = current_y + dy
        if MAZE[new_y][new_x] == "W":
            return
        elif MAZE[new_y][new_x] == "D":
            if len(coins) > 0:
                return
        #Checks for collisions with maze scenery
            elif LEVEL == 5:
                game_complete = True
                game_complete_screen()

            else:
                game_won = True
                game_won_screen()
        #Checks if the thief has collected all the coins

        Coin.coin_collision(new_x,new_y)
        #Calls collect coin method to see if the new coordinate has a coin

        Powerup.apply_powerup(new_x, new_y)

        animate(self, pos = screen_coords(new_y,new_x), duration = THIEF_SPEED, on_finished = repeat_thief_move)
        #Updates thiefs position and allows thief to move smoothly at a set speed

   

def on_key_down(key):
    if key == keys.LEFT or key == keys.A:
        thief.move(-1,0)
    elif key == keys.RIGHT or key == keys.D:
        thief.move(1,0)
    elif key == keys.UP or key == keys.W:
        thief.move(0,-1)
    elif key == keys.DOWN or key == keys.S:
        thief.move(0,1)

def repeat_thief_move():

    if keyboard.LEFT or keyboard.A:
        thief.move(-1,0)

    elif keyboard.RIGHT or keyboard.D:
        thief.move(1,0)

    elif keyboard.UP or keyboard.W:
        thief.move(0,-1)

    elif keyboard.DOWN or keyboard.S:
        thief.move(0,1)

class Enemy(Actor):
    #Inherits Actor class
    def __init__(self, x, y):
        super().__init__("security_guard_left")
        self.anchor = ("left","top")
        self.pos = (x,y)
        #Sets security guard position to the screen coordinates of the current maze position

    def move(self):
        global game_over

        if GAMEMODE == "play":
            (thief_x, thief_y) = maze_coords(thief)
            #Retrives current cooridantes of thief
            (security_guard_x, security_guard_y) = maze_coords(self)
            #Retrives current cooridantes of a security guard
            if thief_x > security_guard_x and MAZE[security_guard_y][security_guard_x + 1] != "W":
                self.image = "security_guard_right"
                security_guard_x += 1
            elif thief_x < security_guard_x and MAZE[security_guard_y][security_guard_x - 1] != "W":
                self.image = "security_guard_left"
                security_guard_x -= 1
            elif thief_y > security_guard_y and MAZE[security_guard_y + 1][security_guard_x] != "W":
                security_guard_y += 1
            elif thief_y < security_guard_y and MAZE[security_guard_y - 1][security_guard_x] != "W":
                security_guard_y -= 1
            #Checks where the thief is in relation to the security guard and checks if updated coordinates is a wall
            animate(self,pos = screen_coords(security_guard_y,security_guard_x), duration = SECURITY_GUARD_SPEED)

            if security_guard_x == thief_x and security_guard_y == thief_y:
                time.sleep(1)
                game_over = True
                game_over_screen()
            #Ends game if theif and security gaurd are on the same coordinate

def move_security_guards():
    for security_guard in security_guards:
        security_guard.move()

class Coin(Actor):
    #Inherits Actor class
    def __init__(self, x, y):
        super().__init__("coin")
        self.anchor = ("left","top")
        self.pos = (x,y)

    def coin_collision(x,y):
        for coin in coins:
            (coin_x, coin_y) = maze_coords(coin)
            if x == coin_x and y == coin_y:
                coins.remove(coin)
                #Removes coins as the thief moves over them
                break

class Powerup(Actor):
    #Inherits Actor class
    def __init__(self,powerup_type, x, y,):
        if powerup_type == "diamond":
            super().__init__("diamond")
        elif powerup_type == "dynamite":
            super().__init__("dynamite")
        #Check what image should be assigned to the powerup

        self.anchor = ("left","top")
        self.pos = (x,y)
        #Sets powerups position to the screen coordinates of the current maze position

    def apply_powerup(x,y):
        global THIEF_SPEED

        for powerup in powerups:
            (powerup_x, powerup_y) = maze_coords(powerup)
            if x == powerup_x and y == powerup_y:
                powerups.remove(powerup)
                #Removes powerup as the thief moves over it
                
                if MAZE[powerup_y][powerup_x] == "A":
                    print("speed up!")
                    THIEF_SPEED = 0.1
                    return THIEF_SPEED
                #Applies speed boost if diamond powerup
                
                elif MAZE [powerup_y][powerup_x] == "B":
                    for y in range(2,len(MAZE)-1):
                        for x in range(1, len(MAZE[0])-1):
                            if random.random() < 0.3:
                                MAZE[y][x] = " "
                #Randomly removes walls

                break
            
def draw_actors():
    thief.draw()

    for security_guard in security_guards:
        security_guard.draw()
        
    for coin in coins:
        coin.draw()
        
    for powerup in powerups:
        powerup.draw()

def on_key_up(key):
    global GAMEMODE, game_over, game_won
    if key == key.SPACE and GAMEMODE == "how to play":
        main_menu()
    #opens main menu screen if the spacebar is pressed when the user is at the how to play menu

    if key == key.M and GAMEMODE == "play":
        main_menu()

    if key == key.R and GAMEMODE == "play":
        if LEVEL == 1:
            level_1()
            setup_actors()
            
        elif LEVEL == 2:
            level_2()
            setup_actors()
 

        elif LEVEL == 3:
            level_3()
            setup_actors()


        elif LEVEL == 4:
            level_4()
            setup_actors()


        elif LEVEL == 5:
            level_5()
            setup_actors()
            
    #Allows user to restart from the current level
  
    if key == key.SPACE and GAMEMODE == "game over":
        if LEVEL == 1:
            level_1()
            setup_actors()
            game_over = False
            
        elif LEVEL == 2:
            level_2()
            setup_actors()
            game_over = False

        elif LEVEL == 3:
            level_3()
            setup_actors()
            game_over = False

        elif LEVEL == 4:
            level_4()
            setup_actors()
            game_over = False

        elif LEVEL == 5:
            level_5()
            setup_actors()
            game_over = False
    #Allows user to restart from the current level

    if key == key.SPACE and GAMEMODE == "game won":
        if LEVEL == 1:
            print("new level")
            level_2()
            setup_actors()
            game_won = False
            
        elif LEVEL == 2:
            print("new level")
            level_3()
            setup_actors()
            game_won = False

        elif LEVEL == 3:
            print("new level")
            level_4()
            setup_actors()
            game_won = False

        elif LEVEL == 4:
            print("new level")
            level_5()
            setup_actors()
            game_won = False
            
    #Allows user to progress to the next level

    if key == key.SPACE and GAMEMODE == "game complete":
        main_menu()

    
def draw():
    draw_background()
    draw_boarder()
    draw_actors()
    draw_timer()
    draw_high_score()
    draw_usability_features()
    
    if GAMEMODE == "main menu":
        screen.clear()
        game_title.draw()
        
        for button in buttons:
            button.draw()
    # game_title and buttons will only be drawn on screen if GAMEMODE is set to "main menu"

    if GAMEMODE == "how to play":
        screen.clear()
        draw_htp()
    
    # draws the text informing the user on how to play screen

    if GAMEMODE == "game over":
        screen.clear()
        game_over_title.draw()
        draw_game_over()
        caught_image.draw()

    #draws text and actors on the game over screen

    if GAMEMODE == "game won":
        screen.clear()
        game_won_title.draw()
        draw_game_won()

    #draws text on the game won screen

    if GAMEMODE == "game complete":
        screen.clear()
        game_complete_title.draw()
        treasure_image.draw()
        draw_game_complete()

    #draws text on the game complete screen

         
game_over = False
game_won = False
game_complete = False
SECURITY_GUARD_SPEED = 0.3
clock.schedule_interval(move_security_guards, SECURITY_GUARD_SPEED)
level_1()
setup_actors()
read_time()
update()
main_menu()
pgzrun.go()

    
