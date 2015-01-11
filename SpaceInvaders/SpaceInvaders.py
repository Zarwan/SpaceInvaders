# Name: Zarwan Hashem
# Date: Jan. 10, 2015
# Description: Space Invaders characters.

#Import statements
import pygame
import random

#Pygame setup
pygame.init()
size = (1000, 600)
screen = pygame.display.set_mode(size)
myClock = pygame.time.Clock()

#Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

#Music
bullet_sound = pygame.mixer.Sound("bullet_sound.wav")
boss_music = pygame.mixer.Sound("boss_level.ogg")
you_win_music = pygame.mixer.Sound ("SIWinMusic.ogg")
game_music = pygame.mixer.Sound("SIGameMusic.ogg")
game_over_music = pygame.mixer.Sound ("game_over.wav")
menu_music = pygame.mixer.Sound ("SpaceInvadersMenu.ogg")

#Fonts
next_level_font = pygame.font.SysFont ("Impact", 50)
game_over_font = pygame.font.SysFont ("Impact", 70)
score_font = pygame.font.SysFont ("Impact", 30)
instructions_heading_font = pygame.font.SysFont ("Poster", 80)
instructions_subheading_font = pygame.font.SysFont ("Poster", 40)
instructions_information_font = pygame.font.SysFont ("Poster", 30)
instructions_controls_font = pygame.font.SysFont ("Poster", 30)
menu_options_font = pygame.font.SysFont ("Impact", 40)

#Text
instructions_controls_one = instructions_controls_font.render("Left Arrow Key = Move Left                                           Right Arrow Key = Move Right", 0, WHITE)
instructions_controls_two = instructions_controls_font.render("Space Key = Shoot", 0, WHITE)
instructions_heading_one = instructions_heading_font.render("How to Play", 0, RED)
instructions_heading_two = instructions_subheading_font.render("Controls", 0, BLUE)
instructions_story_one = instructions_information_font.render("The aliens have invaded! Fight them off before it's too late! There seem to be 3 types of", 0, WHITE)
instructions_story_two = instructions_information_font.render("aliens. The red ones seem to be the weakest, followed by the white ones, and finally the", 0, WHITE)
instructions_story_three = instructions_information_font.render("blue ones. All of the aliens shoot bullets. Their bullets seem to be tied to each aliens life", 0, WHITE)
instructions_story_four = instructions_information_font.render("force, so if the alien dies, their bullet is also destroyed. If you get hit once or run out of", 0, WHITE) 
instructions_story_five = instructions_information_font.render("bullets, it's game over. Good luck.", 0, WHITE)
shot_descrip = instructions_information_font.render(" -> Gives you 4 extra bullets when shot down", 0, WHITE)
speed_descrip = instructions_information_font.render(" -> Speeds up your bullets for the rest of the level", 0, WHITE)
play_game_text = menu_options_font.render("PLAY GAME", 0, BLACK)
instructions_text = menu_options_font.render("INSTRUCTIONS", 0, BLACK)
go_back_text = menu_options_font.render("GO BACK", 0, BLACK)

#Images
space_invaders_logo = pygame.image.load("SpaceInvadersLogo.gif")
rocket_pic = pygame.image.load("rocket_cartoon.png")
star_pic = pygame.image.load("star.png")
new_and_improved = pygame.image.load("new_and_improved.gif")
bullet_pic = pygame.image.load("bullet.jpg")
speed_boost_pic = pygame.image.load("speed_boost.png")


#Main graphics used
def alien_one(x): #Red Alien (Initial x is 310)
    pygame.draw.circle (screen, RED, (x, 310), 50) #Body
    pygame.draw.ellipse (screen, WHITE, pygame.Rect(x - 20, 280, 40, 25)) #Eye, first layer
    pygame.draw.circle (screen, BLACK, (x, 290), 5) #Eye, second layer
    pygame.draw.rect (screen, BLACK, pygame.Rect(x - 20, 320, 40, 20)) #Mouth, first layer
                        
def alien_two(x): #White Alien (Initial x is 100)
    pygame.draw.rect (screen, WHITE, pygame.Rect(x, 150, 50, 50)) #Body
    pygame.draw.rect (screen, RED, pygame.Rect(x + 1, 200, 5, 15)) #Left leg
    pygame.draw.rect (screen, RED, pygame.Rect(x + 5, 210, 5, 15)) #Left leg, part 2
    pygame.draw.rect (screen, RED, pygame.Rect(x + 24, 200, 5, 15)) #Middle leg
    pygame.draw.rect (screen, RED, pygame.Rect(x + 29, 210, 5, 15)) #Middle leg, part 2
    pygame.draw.rect (screen, RED, pygame.Rect(x + 45, 200, 5, 15)) #Right leg
    pygame.draw.rect (screen, RED, pygame.Rect(x + 49, 210, 5, 15)) #Right leg, part two
    pygame.draw.circle (screen, RED, (x + 10, 160), 5) #Left eye
    pygame.draw.circle (screen, RED, (x + 40, 160), 5) #Right eye
    pygame.draw.ellipse (screen, RED, pygame.Rect(x + 10, 175, 30, 15)) #Mouth
                        
def alien_three(x): #Blue Alien (Initial x is 500)
    pygame.draw.rect (screen, BLUE, pygame.Rect(x, 50, 40, 70)) #Body
    pygame.draw.circle (screen, RED, (x + 22, 65), 8) #Eye, first layer
    pygame.draw.circle (screen, BLUE, (x + 22, 66), 5) #Eye, second layer
    pygame.draw.circle (screen, BLACK, (x + 21, 65), 2) #Eye, third layer
    pygame.draw.line (screen, RED, (x + 13, 90), (x + 30, 90), 8) #Mouth
    
def boss_alien(x, y):
    
    #Changes the colour of the boss alien depending on how many times it has been hit
    if boss_lives == 3:
        pygame.draw.rect (screen, WHITE, pygame.Rect(x, y + 50, 30, 50)) #Body
    elif boss_lives == 2:
        pygame.draw.rect (screen, GREEN, pygame.Rect(x, y + 50, 30, 50)) #Body
    else:
        pygame.draw.rect (screen, RED, pygame.Rect(x, y + 50, 30, 50)) #Body
    pygame.draw.line (screen, BLUE, (x + 5, 155), (x + 10, y + 60), 5) #Left eyebrow
    pygame.draw.line (screen, BLUE, (x + 25, 155), (x + 20, y + 60), 5) #Left eyebrow
    pygame.draw.circle (screen, BLACK, (x + 9, y + 66), 3) #Left eye
    pygame.draw.circle (screen, BLACK, (x + 21, y + 66), 3) #Right eye
    pygame.draw.circle (screen, RED, (x + 15, y + 85), 10) #Mouth, layer one
    pygame.draw.circle (screen, WHITE, (x + 15, y + 85), 7) #Mouth, layer two
                        
def player(x):
    pygame.draw.rect (screen, WHITE, pygame.Rect (x, 550, 50, 20))

def player_shot(x, y):
    pygame.draw.circle (screen, WHITE, (x, y), 10)
    
def alien_shot(x, y):
    pygame.draw.circle (screen, BLUE, (x, y), 10)
    
def shot_bonus_draw(x, y):
    pygame.draw.rect (screen, GREEN, pygame.Rect(x, y, 30, 30))
    screen.blit(bullet_pic, pygame.Rect(x + 5, y + 5, 20, 20))
    
def speed_bonus_draw(x, y):
    pygame.draw.rect (screen, GREEN, pygame.Rect(x, y, 30, 30))
    screen.blit(speed_boost_pic, pygame.Rect(x + 5, y + 5, 20, 20))
    
#Constants    
PLAY_BUTTON_X = 150
PLAY_BUTTON_X2 = 400
PLAY_BUTTON_Y = 400
PLAY_BUTTON_Y2 = 500
INSTRUC_BUTTON_X = 600
INSTRUC_BUTTON_X2 = 850
INSTRUC_BUTTON_Y = 400
INSTRUC_BUTTON_Y2 = 500
BACK_BUTTON_X = 700
BACK_BUTTON_X2 = 950
BACK_BUTTON_Y = 480
BACK_BUTTON_Y2 = 580
INITIAL_ALIEN1_SHOT = 325
ALIEN1_LIMIT = 2
INITIAL_ALIEN2_SHOT = 150
INITIAL_ALIEN2_SHOT = 150
INITIAL_ALIEN3_SHOTY = 75
INITIAL_ALIEN3_SHOTX = 50
LEVEL_SHOT_GROUP1 = 3
LEVEL_SHOT_GROUP2 = 7
SHOTS_PER_LEVEL1 = 8
SHOTS_PER_LEVEL2 = 5
SHOTS_PER_LEVEL3 = 3
SHOTS_PER_LEVEL4 = 10
PLAYER_MOVE = 5
PLAYER_SHOT_Y = 565
PLAYER_SHOT_X = 25
MAX_PLAYER_X = 950
MIN_PLAYER_X = 0
ALIEN1_SCORE_INC = 5
ALIEN2_SCORE_INC = 10
SHOT_BONUS_INC = 4
ALIEN2_SHOT_X = 25
ALIEN1_SHOT_SPEED = 4
ALIEN3_MOVE = 5
SHOT_SPEED = 15
SHOT_BOOST_SPEED = 25
LAST_LEVEL = 8
ALIEN2_SHOT_Y = 150
ALIEN1_SHOT_Y = 325
ALIEN2_SHOT_SPEED = 5
POWERUP_INITIAL_Y = 150
BOSS_SCORE_INC = 25
ALIEN_START_X = 50
ALIEN1_SPACING = 300
ALIEN2_SPACING = 400
ALIEN3_SPACING = 400
ALIEN2_LEVELS = 3
ALIEN3_LEVELS = 5
ALIEN1_RADIUS = 50
ALIEN1_Y = 310
SHOT_RADIUS = 10
PLAYER_WIDTH = 50
MIN_SHOT_Y = 10
ALIEN2_WIDTH = 50
ALIEN2_HEIGHT = 200
ALIEN1_LEFT_BORDER = 80
ALIEN2_RIGHT_BORDER = 750
BOSS_SHOTX_CHANGE = 50
ALIEN1_RIGHT_BORDER = 900
POWERUPS_WIDTH = 30
POWERUP_SPEED = 2
ALIEN3_SHOT_Y = 75
MAX_BOSS_LIVES = 3
BOSS_MOVE_RATE1 = 300
BOSS_MOVE_RATE2 = 200
BOSS_MOVE_RATE3 = 150
BOSS_SHOTX_WIDTH = 15
BOSS_WIDTH = 30
BOSS_HEIGHT = 50
POWERUP_MAX_X = 1000
POWERUP_WIDTH = 30
ALIEN3_WIDTH = 40
ALIEN3_SCORE_INC = 15
ALIEN3_HEIGHT = 120
BOSS_HEIGHT = 50
ALIEN2_LEFT_BORDER = 120
BOSS_SHOT_SPEED1 = 4
BOSS_SHOT_SPEED2 = 5
BOSS_SHOT_SPEED3 = 6
MIN_BOSS_X = 200
MAX_BOSS_X = 800
MAX_PLAYER_HEIGHT = 570
MIN_PLAYER_HEIGHT = 540
MAX_ALIEN_SHOTY = 590
BOSS_MIN_SHOTY = 150
ALIEN1_MIN_Y = 260
ALIEN1_MAX_Y = 360
ALIEN2_MIN_Y = 150
ALIEN2_MAX_Y = 200
ALIEN3_MIN_Y = 50
ALIEN3_MAX_Y = 120
ALIEN2_MOVEMENT = 3
ALIEN3_SHOT_SPEED = 6

#Other variables
game_running = True
instructions_running = True
running = False
alien_ones_exist = []
alien_ones_x = []
alien_ones_shooting = []
alien_ones_shoty = []
alien_ones_shotx = []
alien_twos_exist = []
alien_twos_x = []
alien_twos_shooting = []
alien_twos_shoty = []
alien_twos_shotx = []
dead_alien_twos = 0
alien_threes_x = []
alien_threes_shooting = []
alien_threes_shoty = []
alien_threes_shotx = []
dead_alien_threes = 0
alien_threes_exist = []
current_level = 0
game_over = False
you_win = False
player_right = False
player_left = False
shot_fired = False
player_x = 5
shots_left = 0
shot_y = 550
alien_one_left = True
alien_two_left = False
alien_three_left = True
last_level = 1
score = 0 
boss_exist = False
boss_y = 100
boss_x = 200
boss_shotx = [80, 80, 80]
boss_shoty = [150, 150, 150]
boss_shooting = [False, False, False]
boss_lives = 3
boss_left = False
boss_moved = False
shot_bonus = False
shot_bonusy = 260
shot_bonus_x = 1000
shot_bonus_right = True
speed_bonus = False
speed_bonusy = 260
speed_bonus_x = 1000
speed_bonus_right = True
speed_boost_yes = False


#Main game loop, controls the menu options
while game_running:
    
    #Starts menu music and stops other music
    game_music.stop()
    boss_music.stop()
    menu_music.play()
    
    #Checks for events on the menu
    for evnt in pygame.event.get():
        
            #If the window has been closed
            if evnt.type == pygame.QUIT:
                game_running = False
                
            #Checks if the user has chosen to play the game    
            if evnt.type == pygame.MOUSEBUTTONDOWN and evnt.button == 1:
                if evnt.pos[0] >= PLAY_BUTTON_X and evnt.pos[0] <= PLAY_BUTTON_X2 and evnt.pos[1] >= PLAY_BUTTON_Y and evnt.pos[1] <= PLAY_BUTTON_Y2:
                    menu_music.stop() #Stops the menu music
                    
                    #Resets variables used everytime the game is played
                    running = True
                    game_over = False
                    you_win = False
                    current_level = 0
                    last_level = 1
                    player_right = False
                    player_left = False
                    player_x = 0
                    shot_bonus = False
                    speed_bonus = False
                    alien_one_left = True
                    alien_two_left = False
                    alien_three_left = True
                    speed_boost_yes = False
                    shot_fired = False
                    shot_y = PLAYER_SHOT_Y
                    score = 0
                    boss_lives = MAX_BOSS_LIVES
                    screen.fill(BLACK)
                    
                    #Prints the initial level
                    level_text = next_level_font.render("Level", 0, BLUE)
                    screen.blit(level_text, pygame.Rect(400, 200, 100, 100))
                    level_num = str(current_level + 1)
                    level_num_text = next_level_font.render(level_num, 0, BLUE)
                    screen.blit(level_num_text, pygame.Rect(550, 200, 100, 100))
                    
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    
                    #Controls the changing of levels
                    while running:
                        
                        #Stops the game music, the restarts it depending on the level
                        game_music.stop() 
                        if current_level < LAST_LEVEL - 1:
                            game_music.play() 
                        else:
                            boss_music.play()
                           
                        #Resets variables used in every level
                        current_level += 1
                        alien_ones_exist = []
                        alien_ones_x = []
                        alien_ones_shooting = []
                        alien_ones_shoty = []
                        alien_ones_shotx = []
                        dead_alien_ones = 0
                        alien_twos_exist = []
                        alien_twos_x = []
                        alien_twos_shooting = []
                        alien_twos_shoty = []
                        alien_twos_shotx = []
                        dead_alien_twos = 0
                        alien_threes_x = []
                        alien_threes_shooting = []
                        alien_threes_shoty = []
                        alien_threes_shotx = []
                        dead_alien_threes = 0
                        alien_threes_exist = []
                        speed_boost_yes = False
                        shots_left = 0
                        player_x = 0
                        shot_bonus = False
                        speed_bonus = False
                        
                        
                        #Changes the amount of aliens depending on the level
                        if current_level < LAST_LEVEL:
                            
                            #Changes the amount of red aliens depending on the level
                            for i in range(0, current_level):
                                alien_ones_exist += [True]
                                alien_ones_x += [(ALIEN_START_X + (ALIEN1_SPACING * (i + 1)))]
                                alien_ones_shooting += [False]
                                alien_ones_shoty += [INITIAL_ALIEN1_SHOT]
                                alien_ones_shotx += [INITIAL_ALIEN1_SHOT]
                                shots_left += 1
                                
                                #Limits the number of aliens
                                if len(alien_ones_exist) > ALIEN1_LIMIT:
                                    break
                                
                            #Changes the amount of white aliens depending on the level    
                            if current_level > ALIEN2_LEVELS:    
                                for i in range(0, (current_level - ALIEN2_LEVELS)):
                                    alien_twos_exist += [True]
                                    alien_twos_x += [(ALIEN_START_X + (ALIEN2_SPACING * (i + 1)))]
                                    alien_twos_shooting += [False]
                                    alien_twos_shoty += [INITIAL_ALIEN2_SHOT]
                                    alien_twos_shotx += [INITIAL_ALIEN2_SHOT]
                                    shots_left += 1
                                    
                                    #Limits the number of aliens
                                    if len(alien_twos_exist) > 1:
                                        break
                                    
                            #Changes the amount of blue aliens depending on the level   
                            if current_level > ALIEN3_LEVELS:  
                                for i in range(0, (current_level - ALIEN3_LEVELS)):
                                    alien_threes_exist += [True]
                                    alien_threes_x += [(ALIEN_START_X + (ALIEN3_SPACING * (i + 1)))]
                                    alien_threes_shooting += [False]
                                    alien_threes_shoty += [INITIAL_ALIEN3_SHOTY]
                                    alien_threes_shotx += [INITIAL_ALIEN3_SHOTX]
                                    shots_left += 1
                                    
                                    #Limits the number of aliens
                                    if len(alien_threes_exist) > 1:
                                        break
                                    
                            #Sets the amount of shots per level
                            if current_level <= LEVEL_SHOT_GROUP1:
                                shots_left += SHOTS_PER_LEVEL1
                            elif current_level > LEVEL_SHOT_GROUP1 and current_level <= LEVEL_SHOT_GROUP2:
                                shots_left += SHOTS_PER_LEVEL2
                            elif current_level > LEVEL_SHOT_GROUP2:
                                shots_left += SHOTS_PER_LEVEL3
                                
                        else:
                            #Sets the amount of shots if the level is the last level (the boss level) and activates the boss alien
                            shots_left += SHOTS_PER_LEVEL4
                            boss_exist = True
                            
                        #Resets the loop bools
                        game_over = False
                        you_win = False                        
                        
                        #Controls how each level works
                        while game_over == False and you_win == False:
                            
                            #Checks for events
                            for evnt in pygame.event.get():
                                
                                #Checks if the user has closed the window
                                if evnt.type == pygame.QUIT:
                                    game_over = True
                                    running = False
                                    game_running = False
                                
                                #Player movement input
                                if evnt.type == pygame.KEYUP and evnt.key == pygame.K_RIGHT:
                                    player_right = False
                                if evnt.type == pygame.KEYUP and evnt.key == pygame.K_LEFT:
                                    player_left = False
                                if evnt.type == pygame.KEYDOWN:
                                    if evnt.key == pygame.K_RIGHT:
                                        player_right = True
                                    if evnt.key == pygame.K_LEFT:
                                        player_left = True
                                    if evnt.key == pygame.K_SPACE:
                                        shot_fired = True
                                        
                            screen.fill(BLACK) #Clears the screen
                            
                            #Player movement adjustments
                            if player_right == True and player_x != MAX_PLAYER_X:
                                player_x += PLAYER_MOVE
                            if player_left == True and player_x != MIN_PLAYER_X:
                                player_x -= PLAYER_MOVE
                            player(player_x)
                            
                            #Player Shooting
                            if current_level != last_level: #Checks if it's a new level, and resets the shot variables
                                last_level = current_level
                                shot_fired = False
                                shot_y = PLAYER_SHOT_Y
                                
                            #If a shot has been fired    
                            if shot_fired == True and shots_left > 0:
                                
                                #Resets the player shot x
                                if shot_y >= PLAYER_SHOT_Y:
                                    shot_x = player_x + PLAYER_SHOT_X
                                    bullet_sound.play()
                                player_shot(shot_x, shot_y) #Outputs the shot
                                
                                #If this isn't the last level (So there is no boss alien)
                                if current_level < LAST_LEVEL:
                                    
                                    #Checks if the shot has hit any red aliens, if it has, removes the alien and resets the shooting variables
                                    for j in range(0, len(alien_ones_exist)):
                                        if alien_ones_exist[j] == True:
                                            
                                            #Red alien collision
                                            if shot_x <= alien_ones_x[j] + ALIEN1_RADIUS and shot_x >= alien_ones_x[j] - ALIEN1_RADIUS and shot_y >= ALIEN1_Y - ALIEN1_RADIUS and shot_y <= ALIEN1_Y + ALIEN1_RADIUS:
                                                #Resets shot variables, increases the score, kills the alien, and removes a shot
                                                shot_y = PLAYER_SHOT_Y
                                                shots_left -= 1
                                                alien_ones_exist[j] = False
                                                score += ALIEN1_SCORE_INC
                                                shot_fired = False
                                                dead_alien_ones += 1
                                                break
                                                
                                            
                                    #Checks if the shot has hit any white aliens, if it has, removes the alien and resets the shooting variables
                                    if len(alien_twos_exist) >= 1:
                                        for p in range(0, len(alien_twos_exist)):
                                            if alien_twos_exist[p] == True:
                                                
                                                #White alien collision
                                                if ((shot_x - SHOT_RADIUS <= alien_twos_x[p] + ALIEN2_WIDTH and shot_x - SHOT_RADIUS >= alien_twos_x[p]) or (shot_x + SHOT_RADIUS >= alien_twos_x[p] and shot_x + SHOT_RADIUS <= alien_twos_x[p] + ALIEN2_WIDTH)) and shot_y + SHOT_RADIUS <= ALIEN2_HEIGHT:
                                                    #Resets shot variables, increases the score, kills the alien, and removes a shot
                                                    shot_y = PLAYER_SHOT_Y
                                                    shots_left -= 1
                                                    alien_twos_exist[p] = False
                                                    score += ALIEN2_SCORE_INC
                                                    shot_fired = False
                                                    dead_alien_twos += 1
                                                    break
                                              
                                    #Checks if the shot has hit any blue aliens, if it has, removes the alien and resets the shooting variables
                                    if len(alien_threes_exist) >= 1:
                                        for n in range(0, len(alien_threes_exist)):
                                            if alien_threes_exist[n] == True:
                                                
                                                #Blue alien collision
                                                if ((shot_x - SHOT_RADIUS <= alien_threes_x[n] + ALIEN3_WIDTH and shot_x - SHOT_RADIUS >= alien_threes_x[n]) or (shot_x + SHOT_RADIUS >= alien_threes_x[n] and shot_x + SHOT_RADIUS <= alien_threes_x[n] + ALIEN3_WIDTH)) and shot_y <= ALIEN3_HEIGHT:
                                                    #Resets shot variables, increases the score, kills the alien, and removes a shot
                                                    shot_y = PLAYER_SHOT_Y
                                                    shots_left -= 1
                                                    alien_threes_exist[n] = False
                                                    score += ALIEN3_SCORE_INC
                                                    shot_fired = False
                                                    dead_alien_threes += 1
                                                    break
                                                
                                else:
                                    #Checks if the shot has hit the boss alien, removes lives if it has, and resets the shooting variables
                                    if ((shot_x - SHOT_RADIUS <= boss_x + BOSS_WIDTH and shot_x - SHOT_RADIUS >= boss_x)  or (shot_x + SHOT_RADIUS >= boss_x and shot_x + SHOT_RADIUS <= boss_x + BOSS_WIDTH)) and shot_y <= boss_y + BOSS_HEIGHT:
                                        #Resets shot variables, increases the score, lowers the boss lives, and removes a shot
                                        boss_lives -= 1
                                        shot_y = PLAYER_SHOT_Y
                                        score += ALIEN1_SCORE_INC
                                        shot_fired = False
                                        shots_left -= 1
                                        
                                        #Kills the boss if all of its lives are gone
                                        if boss_lives <= 0:
                                            boss_exist = False
                                            score += BOSS_SCORE_INC
                                            
                                #Checks if the ammo powerup is in play and checks if the shot hit the powerup
                                if shot_bonus == True and ((shot_x - SHOT_RADIUS <= shot_bonusx + POWERUP_WIDTH and shot_x - SHOT_RADIUS >= shot_bonusx) or (shot_x + SHOT_RADIUS >= shot_bonusx and shot_x + SHOT_RADIUS <= shot_bonusx + POWERUPS_WIDTH)) and shot_y - SHOT_RADIUS <= shot_bonusy + POWERUPS_WIDTH:
                                    
                                        #Activates powerups and resets variables
                                        shots_left += SHOT_BONUS_INC
                                        shot_bonus = False
                                        shot_y = PLAYER_SHOT_Y
                                        shot_fired = False
                                    
                                #Checks if the speed powerup is in play and checks if the shot hit the powerup
                                if speed_bonus == True and ((shot_x - SHOT_RADIUS <= speed_bonusx + POWERUP_WIDTH and shot_x - SHOT_RADIUS >= speed_bonusx) or (shot_x + SHOT_RADIUS >= speed_bonusx and shot_x + SHOT_RADIUS <= speed_bonusx + POWERUPS_WIDTH)) and shot_y - SHOT_RADIUS <= speed_bonusy + POWERUPS_WIDTH:
                                    
                                    #Activates powerups and resets variables
                                    speed_boost_yes = True
                                    speed_bonus = False
                                    shot_y = PLAYER_SHOT_Y
                                    shots_left -= 1
                                    shot_fired = False
                                
                                #Adjusts the shot speed if the powerup is in effect
                                if speed_boost_yes == True and shot_fired == True:
                                    if speed_level == current_level:
                                        shot_y -= SHOT_BOOST_SPEED
                                    else:
                                        speed_boost_yes = False
                                
                                #Moves the shot if the powerup isn't in effect
                                if speed_boost_yes == False and shot_fired == True:
                                    shot_y -= SHOT_SPEED
                                    
                                #Resets the shot if it goes off screen
                                if shot_fired == True:
                                    if shot_y < MIN_SHOT_Y:
                                        shot_y = PLAYER_SHOT_Y
                                        shots_left -= 1 #Limited shots
                                        shot_fired = False
                    
                                        
                            if current_level < LAST_LEVEL: #Checks to see if it is the boss level. If not, move the other types of aliens (not the boss type)
            
                                #Red alien movement
                                for o in range(0, len(alien_ones_exist)): #Goes through the list of red aliens
                                    if alien_ones_exist[o] == True:
                                        
                                        #Make sure the aliens don't move off the screen before moving them
                                        if alien_one_left == True and alien_ones_x[o] >= ALIEN1_LEFT_BORDER:
                                            alien_ones_x[o] -= 1
                                        else:
                                            alien_one_left = False
                                            
                                        if alien_one_left == False and alien_ones_x[o] <= ALIEN1_RIGHT_BORDER:
                                            alien_ones_x[o] += 1
                                        else:
                                            alien_one_left = True
                                        
                                #White alien movement
                                if len(alien_twos_exist) >= 1:
                                    for k in range(0, len(alien_twos_exist)): #Goes through the list of white aliens
                                        if alien_twos_exist[k] == True:
                                            
                                            #Make sure the aliens don't move off the screen before moving them
                                            if alien_two_left == True and alien_twos_x[k] >= ALIEN2_LEFT_BORDER:
                                                alien_twos_x[k] -= ALIEN2_MOVEMENT
                                            else:
                                                alien_two_left = False
                                                
                                            if alien_two_left == False and alien_twos_x[k] <= ALIEN2_RIGHT_BORDER:
                                                alien_twos_x[k] += ALIEN2_MOVEMENT
                                            else:
                                                alien_two_left = True
                                                
                                #Blue alien movement
                                if len(alien_threes_exist) >= 1:
                                    for k in range(0, len(alien_threes_exist)): #Goes through the list of blue aliens
                                        
                                        #Make sure the aliens don't move off the screen before moving them
                                        if alien_threes_exist[k] == True:
                                            if alien_three_left == True and alien_threes_x[k] >= 100:
                                                alien_threes_x[k] -= ALIEN3_MOVE
                                            else:
                                                alien_three_left = False
                                                
                                            if alien_three_left == False and alien_threes_x[k] <= 800:
                                                alien_threes_x[k] += ALIEN3_MOVE
                                            else:
                                                alien_three_left = True
                                                
        
                                    
                                #Draws red aliens
                                for y in range(0, len(alien_ones_exist)):
                                    if alien_ones_exist[y] == True: #Checks if they are still alive before drawing them
                                        alien_one(alien_ones_x[y])
                                             
                                #Draws white aliens
                                if len(alien_twos_exist) >= 1:
                                    for y in range(0, len(alien_twos_exist)):
                                        if alien_twos_exist[y] == True: #Checks if they are still alive before drawing them
                                            alien_two(alien_twos_x[y])
                                            
                                #Draws blue aliens
                                if len(alien_threes_exist) >= 1:
                                    for y in range(0, len(alien_threes_exist)):
                                        if alien_threes_exist[y] == True: #Checks if they are still alive before drawing them
                                            alien_three(alien_threes_x[y])
                                        
                                            
                                #Checks if all of the aliens are dead, and resets the variables if they are
                                if dead_alien_ones == len(alien_ones_exist) and dead_alien_twos == len(alien_twos_exist) and dead_alien_threes == len(alien_threes_exist):
                                    dead_alien_ones = 0
                                    dead_alien_twos = 0
                                    dead_alien_threes = 0
                                    you_win = True
                                    screen.fill(BLACK)
                                    
                                    #Prints the next level
                                    level_text = next_level_font.render("Level", 0, BLUE)
                                    screen.blit(level_text, pygame.Rect(400, 200, 100, 100))
                                    level_num = str(current_level + 1)
                                    level_num_text = next_level_font.render(level_num, 0, BLUE)
                                    screen.blit(level_num_text, pygame.Rect(550, 200, 100, 100))
                                    
                                    pygame.display.flip()
                                    pygame.time.wait(2000)
                                    
                            else:
                                if boss_exist == False: #Checks if the boss is dead (and it's the last level)
                                    you_win = True
                                else:
                                    #Boss alien movement
                                    if boss_exist == True:
                                        if boss_moved == True: #If the boss is moving
                                            boss_move = random.randint(50, 200) #Randomly moves the boss
                                            
                                            #Make sure the boss doesn't go off screen before it moves
                                            if boss_left == True and (boss_x - boss_move) >= MIN_BOSS_X:
                                                boss_x -= boss_move
                                            else:
                                                boss_left = False
                                                
                                            if boss_left == False and ((boss_x + BOSS_WIDTH) + boss_move) <= MAX_BOSS_X: 
                                                boss_x += boss_move
                                            else:
                                                boss_left = True
                                            boss_moved = False
                                        else: #Randomly decides if the boss should move
                                            
                                            #Adjusts the boss difficulity depending on how many lives it has
                                            #Changes how often the boss moves
                                            if boss_lives == MAX_BOSS_LIVES:
                                                boss_move_frequency = BOSS_MOVE_RATE1
                                            elif boss_lives == MAX_BOSS_LIVES - 1:
                                                boss_move_frequency = BOSS_MOVE_RATE2
                                            else:
                                                boss_move_frequency = BOSS_MOVE_RATE3

                                            #Activates the boss moving
                                            if random.randint(1, boss_move_frequency) == 3:
                                                boss_moved = True
                                        boss_alien(boss_x, boss_y) #Outputs the boss

                                        
                            if current_level < LAST_LEVEL: #If the current level is not the last (so it doesn't have the boss alien)
                                
                                #Red alien shooting
                                for r in range(0, len(alien_ones_exist)):
                                    if alien_ones_exist[r] == True: #Checks if the alien is alive
                                        if alien_ones_shooting[r] == True: #If the alien is currently shooting
                                            if alien_ones_shoty[r] == ALIEN1_SHOT_Y: #Resets the shot y if the alien just shot
                                                alien_ones_shotx[r] = alien_ones_x[r]
                                            alien_shot(alien_ones_shotx[r], alien_ones_shoty[r]) #Outputs the shot
                                            
                                            #Checks for player collision
                                            if alien_ones_shotx[r] + SHOT_RADIUS >= player_x and alien_ones_shotx[r] - SHOT_RADIUS <= player_x + PLAYER_WIDTH and alien_ones_shoty[r] - SHOT_RADIUS <= MAX_PLAYER_HEIGHT and alien_ones_shoty[r] + SHOT_RADIUS >= MIN_PLAYER_HEIGHT:
                                                
                                                #Turns off the game bools (ends the game)
                                                game_over = True
                                                running = False
                                                
                                            #Moves the shot    
                                            alien_ones_shoty[r] += ALIEN1_SHOT_SPEED
                                            
                                            #Resets the shot if it goes off the screen
                                            if alien_ones_shoty[r] >= MAX_ALIEN_SHOTY:
                                                alien_ones_shoty[r] = ALIEN1_SHOT_Y
                                                alien_ones_shooting[r] = False
                                                                   
                                        else: #Randomly decides if the alien should shoot
                                            if random.randint(1, 50) == 3:
                                                alien_ones_shooting[r] = True 
                                           
                                                
                                                
                                #White alien shooting
                                if len(alien_twos_exist) >= 1:
                                    for d in range(0, len(alien_twos_exist)):
                                        if alien_twos_exist[d] == True and alien_twos_shooting[d] == True:
                                            if alien_twos_shoty[d] == ALIEN2_SHOT_Y:
                                                alien_twos_shotx[d] = (alien_twos_x[d] + ALIEN2_SHOT_X)
                                            alien_shot(alien_twos_shotx[d], alien_twos_shoty[d])
                                            
                                            #Checks for player collision
                                            if alien_twos_shotx[d] + SHOT_RADIUS >= player_x and alien_twos_shotx[d] - SHOT_RADIUS <= player_x + PLAYER_WIDTH and alien_twos_shoty[d] - SHOT_RADIUS <= MAX_PLAYER_HEIGHT and alien_twos_shoty[d] + SHOT_RADIUS >= MIN_PLAYER_HEIGHT:
                                                
                                                #Turns off the game bools (ends the game)
                                                game_over = True
                                                running = False
                                            
                                            #Moves the shot
                                            alien_twos_shoty[d] += ALIEN2_SHOT_SPEED
                                            
                                            #Resets the shot if it goes off the screen
                                            if alien_twos_shoty[d] >= 590:
                                                alien_twos_shoty[d] = ALIEN2_SHOT_Y
                                                alien_twos_shooting[d] = False
                                                
                                        else: #Randomly decides if the alien should shoot
                                            if random.randint(1, 30) == 3:
                                                alien_twos_shooting[d] = True 
                                                
                                #Blue alien shooting
                                if len(alien_threes_exist) >= 1:
                                    for d in range(0, len(alien_threes_exist)):
                                        if alien_threes_exist[d] == True and alien_threes_shooting[d] == True:
                                            if alien_threes_shoty[d] == ALIEN3_SHOT_Y:
                                                alien_threes_shotx[d] = alien_threes_x[d] + 20
                                            alien_shot(alien_threes_shotx[d], alien_threes_shoty[d])
                                            
                                            #Checks for player collision
                                            if alien_threes_shotx[d] + SHOT_RADIUS >= player_x and alien_threes_shotx[d] - SHOT_RADIUS <= player_x + PLAYER_WIDTH and alien_threes_shoty[d] - SHOT_RADIUS <= MAX_PLAYER_HEIGHT and alien_threes_shoty[d] + SHOT_RADIUS >= MIN_PLAYER_HEIGHT:
                                                game_over = True
                                                running = False
                                            
                                            #Moves the shot
                                            alien_threes_shoty[d] += ALIEN3_SHOT_SPEED
                                            
                                            #Resets the shot if it goes off the screen
                                            if alien_threes_shoty[d] >= MAX_ALIEN_SHOTY:
                                                alien_threes_shoty[d] = ALIEN3_SHOT_Y
                                                alien_threes_shooting[d] = False
                                                
                                        else: #Randomly decides if the alien should start shooting
                                            if random.randint(1, 21) == 3:
                                                alien_threes_shooting[d] = True 
                                                
                            else:
                                #Boss alien Shooting
                                if boss_exist == True:
                                    for i in range(0, 3):
                                        if boss_shooting[i] == True:
                                            
                                            #Makes the boss shoot 3 shots at once
                                            if boss_shoty[i] == BOSS_MIN_SHOTY:
                                                if i == 0:
                                                    boss_shotx[i] = (boss_x + BOSS_SHOTX_WIDTH) - BOSS_SHOTX_CHANGE
                                                elif i == 1:
                                                    boss_shotx[i] = boss_x + BOSS_SHOTX_WIDTH
                                                elif i == 2:
                                                    boss_shotx[i] = (boss_x + BOSS_SHOTX_WIDTH) + BOSS_SHOTX_CHANGE
                                            alien_shot(boss_shotx[i], boss_shoty[i])
                                            
                                            #Checks for player collision
                                            if boss_shotx[i] + SHOT_RADIUS >= player_x and boss_shotx[i] - SHOT_RADIUS <= player_x + PLAYER_WIDTH and boss_shoty[i] + SHOT_RADIUS >= MIN_PLAYER_HEIGHT:
                                                game_over = True
                                                running = False
                                                
                                            #Increases speed based on the boss lives    
                                            if boss_lives == MAX_BOSS_LIVES:
                                                boss_shoty[i] += BOSS_SHOT_SPEED1
                                            elif boss_lives == 2:
                                                boss_shoty[i] += BOSS_SHOT_SPEED2
                                            else:
                                                boss_shoty[i] += BOSS_SHOT_SPEED3
                                                
                                            #Resets the shot if it moves off the screen    
                                            if boss_shoty[i] >= MAX_ALIEN_SHOTY:
                                                boss_shoty[i] = BOSS_MIN_SHOTY
                                                boss_shooting[i] = False
                                                
                                        else: #Randomly decides if the boss should shoot
                                            if random.randint(1, 3) == 3:
                                                boss_shooting[i] = True 
                                                
                            #Shot Bonus Powerup code
                            #If the powerup isn't in play
                            if shot_bonus == False and random.randint (1, 5000) == 3:
                            
                                #Resets the powerup, and activates it
                                shot_bonus = True
                                shot_bonusy = ALIEN1_MIN_Y
                                
                                #Keeps changing the location of the powerup until it won't hit the alien bodies
                                while True:
                                    if ((shot_bonusy > ALIEN1_MIN_Y and shot_bonusy < ALIEN1_MAX_Y) or (shot_bonusy > ALIEN2_MIN_Y and shot_bonusy < ALIEN2_MAX_Y) or (shot_bonusy > ALIEN3_MIN_Y and shot_bonusy < ALIEN3_MAX_Y)) or ((shot_bonusy + POWERUP_WIDTH > ALIEN1_MIN_Y and shot_bonusy + POWERUP_WIDTH < ALIEN1_MAX_Y) or (shot_bonusy + POWERUP_WIDTH > ALIEN2_MIN_Y and shot_bonusy + POWERUP_WIDTH < ALIEN2_MAX_Y) or (shot_bonusy + POWERUP_WIDTH > ALIEN3_MIN_Y and shot_bonusy + POWERUP_WIDTH < ALIEN3_MAX_Y)):
                                        shot_bonusy = random.randint (200, 500)
                                    else:
                                        break
                                
                                #Decides which side of the screen the powerup will come from
                                if random.randint (0, 1) == 0:
                                    shot_bonusx = 0 - POWERUP_WIDTH
                                    shot_bonus_right = True
                                else:
                                    shot_bonusx = POWERUP_MAX_X
                                    shot_bonus_right = False
                                    
                            #If powerup is already in play       
                            elif shot_bonus == True:
                                
                                #Moves the powerup across the screen 
                                if shot_bonus_right == True:
                                    shot_bonusx += POWERUP_SPEED
                                else:
                                    shot_bonusx -= POWERUP_SPEED
                                    
                                shot_bonus_draw(shot_bonusx, shot_bonusy) #Draws the powerup
                                
                                #Turns off the powerup if it reaches the other side of the screen without being shot
                                if shot_bonusx <= 0 or shot_bonusx >= POWERUP_MAX_X:
                                    shot_bonus = False
                                    
                                    
                                    
                            #Speed Bonus Powerup
                            #If the powerup isn't in play
                            if speed_bonus == False and random.randint (1, 5000) == 3 and speed_boost_yes == False:
                                
                                #Resests and activates the powerup
                                speed_bonus = True
                                speed_level = current_level
                                speed_bonusy = POWERUP_INITIAL_Y
                                
                                #Keeps changing the height of the powerup until it won't hit the alien bodies
                                while True:
                                    if ((speed_bonusy > ALIEN1_MIN_Y and speed_bonusy < ALIEN1_MAX_Y) or (speed_bonusy > ALIEN2_MIN_Y and speed_bonusy < ALIEN2_MAX_Y) or (speed_bonusy > ALIEN3_MIN_Y and speed_bonusy < ALIEN3_MAX_Y)) or ((speed_bonusy + POWERUP_WIDTH > ALIEN1_MIN_Y and speed_bonusy + POWERUP_WIDTH < ALIEN1_MAX_Y) or (speed_bonusy + POWERUP_WIDTH > ALIEN2_MIN_Y and speed_bonusy + POWERUP_WIDTH < ALIEN2_MAX_Y) or (speed_bonusy + POWERUP_WIDTH > ALIEN3_MIN_Y and speed_bonusy + POWERUP_WIDTH < ALIEN3_MAX_Y)):
                                        speed_bonusy = random.randint (200, 500)
                                    else:
                                        break
                                    
                                #Decides which side of the screen the powerup will come from
                                if random.randint (0, 1) == 0:
                                    speed_bonusx = 0 - POWERUP_WIDTH
                                    speed_bonus_right = True
                                else:
                                    speed_bonusx = POWERUP_MAX_X
                                    speed_bonus_right = False
                                    
                            #If the powerup is already activated          
                            elif speed_bonus == True:
                                
                                #Moves the powerup across the screen 
                                if speed_bonus_right == True:
                                    speed_bonusx += POWERUP_SPEED
                                else:
                                    speed_bonusx -= POWERUP_SPEED
                                    
                                speed_bonus_draw(speed_bonusx, speed_bonusy) #Draws the powerup
                                
                                #Turns off the powerup if it reaches the other side of the screen without being shot
                                if speed_bonusx <= 0 or speed_bonusx >= POWERUP_MAX_X:
                                    speed_bonus = False
                                
                                            
                            #Score Output
                            score_output = str(score)
                            score_text = score_font.render("Your Score: ", 0, RED)
                            screen.blit(score_text, pygame.Rect(20, 20, 100, 100))
                            score_text_two = score_font.render(score_output, 0, RED)
                            screen.blit(score_text_two, pygame.Rect(220, 20, 100, 100))
                            
                            #Shot Output
                            shots_output = str(shots_left)
                            shots_text = score_font.render("Shots Left: ", 0, RED)
                            screen.blit(shots_text, pygame.Rect(800, 20, 100, 100))
                            shots_text_two = score_font.render(shots_output, 0, RED)
                            screen.blit(shots_text_two, pygame.Rect(950, 20, 100, 100))
                            
                            
                            #If the game has been won
                            if you_win == True and current_level >= LAST_LEVEL:
                                
                                #Changes the music
                                game_music.stop()
                                boss_music.stop()
                                you_win_music.play()
                                
                                #Stops playing the game, and clears the screen
                                running = False
                                screen.fill(BLACK)
                                
                                #Outputs the win statement
                                win_text = game_over_font.render("YOU WIN!", 0, RED)
                                screen.blit(win_text, pygame.Rect(370, 200, 100, 100))
                                
                                #Various delays in order to let the "you win" music play
                                pygame.display.flip()
                                pygame.time.wait(3500)
                                you_win_music.stop()
                                pygame.time.wait(1000)

                                
                            #If the game has been lost
                            elif game_over == True or shots_left == 0:
                                
                                #Stops the music
                                game_music.stop()
                                boss_music.stop()
                                
                                #Clears the game screen
                                screen.fill(BLACK)
                                
                                #Outputs the game over statement
                                game_over_text = game_over_font.render("Game Over!", 0, RED)
                                screen.blit(game_over_text, pygame.Rect(350, 200, 100, 100))
                                
                                #Outputs the score
                                score_output = str(score)
                                score_text = score_font.render("Your Score: ", 0, RED)
                                screen.blit(score_text, pygame.Rect(20, 20, 100, 100))
                                score_text_two = score_font.render(score_output, 0, RED)
                                screen.blit(score_text_two, pygame.Rect(220, 20, 100, 100))
                                pygame.display.flip()
                                game_over_music.play() #Plays the game over music
                                pygame.time.wait(3500)
                                game_over_music.stop()
                                game_over = False
                                running = False
                                break
                            
                                            
                            pygame.display.flip()
                            
                            #Changes the delay depending on if the game is over or not
                            if game_over == True or (you_win == True and current_level >= 8):
                                pygame.time.wait(4000)
                            else:
                                myClock.tick(100)
                    
                            
                #IF player has chosen to read the instructions from the menu                
                elif evnt.pos[0] >= INSTRUC_BUTTON_X and evnt.pos[0] <= INSTRUC_BUTTON_X2 and evnt.pos[1] >= INSTRUC_BUTTON_Y and evnt.pos[1] <= INSTRUC_BUTTON_Y2:
                    instructions_running = True
                    
                    #Instructions Screen Loop
                    while instructions_running:
                        
                        #Checks for events
                        for evnt in pygame.event.get():
                            
                            #If the window has been closed
                            if evnt.type == pygame.QUIT:
                                instructions_running = False
                                game_running = False
                                
                            #If the GO BACK button has been pressed
                            if evnt.type == pygame.MOUSEBUTTONDOWN and evnt.button == 1:
                                if evnt.pos[0] >= BACK_BUTTON_X and evnt.pos[0] <= BACK_BUTTON_X2 and evnt.pos[1] >= BACK_BUTTON_Y and evnt.pos[1] <= BACK_BUTTON_Y2:
                                    instructions_running = False
                        
                                    
                        #Outputs the instructions screen
                        screen.fill(BLACK)
                        screen.blit(instructions_heading_one, pygame.Rect(0, 0, 100, 50))
                        screen.blit(instructions_story_one, pygame.Rect(50, 100, 100, 50))
                        screen.blit(instructions_story_two, pygame.Rect(50, 120, 100, 50))
                        screen.blit(instructions_story_three, pygame.Rect(50, 140, 100, 50))
                        screen.blit(instructions_story_four, pygame.Rect(50, 160, 100, 50))
                        screen.blit(instructions_heading_two, pygame.Rect(50, 400, 100, 50))
                        screen.blit(instructions_controls_one, pygame.Rect(100, 450, 100, 50))
                        screen.blit(instructions_controls_two, pygame.Rect(100, 470, 100, 50))
                        pygame.draw.rect(screen, RED, pygame.Rect(700, 480, 250, 100))
                        screen.blit(go_back_text, pygame.Rect(758, 505, 100, 100))
                        pygame.draw.rect (screen, GREEN, pygame.Rect(50, 250, 30, 30))
                        screen.blit(bullet_pic, pygame.Rect(50 + 5, 250 + 5, 20, 20))
                        screen.blit(shot_descrip, pygame.Rect(80, 260, 50, 100))
                        pygame.draw.rect (screen, GREEN, pygame.Rect(50, 300, 30, 30))
                        screen.blit(speed_boost_pic, pygame.Rect(50 + 5, 300 + 5, 20, 20))
                        screen.blit(speed_descrip, pygame.Rect(80, 310, 50, 100))
                        screen.blit(instructions_story_five, pygame.Rect(50, 180, 100, 50))
                        pygame.display.flip()
                        
    #Outputs the main menu            
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, pygame.Rect(150, 400, 250, 100))
    pygame.draw.rect(screen, BLUE, pygame.Rect(600, 400, 250, 100))
    screen.blit(play_game_text, pygame.Rect(187, 424, 100, 100))
    screen.blit(instructions_text, pygame.Rect(608, 424, 100, 100))
    screen.blit(space_invaders_logo, pygame.Rect(282, 0, 100, 100))
    screen.blit(rocket_pic, pygame.Rect(100, 200, 100, 100))
    screen.blit(star_pic, pygame.Rect(100, 100, 50, 50))
    screen.blit(star_pic, pygame.Rect(900, 100, 50, 50))
    screen.blit(new_and_improved, pygame.Rect(900, 500, 100, 100))
    pygame.display.flip()
    
pygame.quit()