import os
import pygame , sys
from pygame.constants import K_DOWN, K_LEFT,K_RIGHT, K_UP, K_a, K_d, K_s, K_w
pygame.font.init()
pygame.mixer.init()

yellow = 0
red = 0



FPS = 60
red_hit = pygame.USEREVENT +1
yellow_hit = pygame.USEREVENT +2

Health_font = pygame.font.SysFont("Arial",20,True)
Winner_font = pygame.font.SysFont("comicsans",100,True)
Winner_font2 = pygame.font.SysFont("comicsans",30,True)

caption = "Space Invaders!"
HEIGHT, WIDTH = 900, 500
WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption(caption)
icon = pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
pygame.display.set_icon(icon)

Shoot_sound = pygame.mixer.Sound(os.path.join("Assets","Grenade+1.mp3"))
hit_sound = pygame.mixer.Sound(os.path.join("Assets","Gun+Silencer.mp3"))

Background_colour = (255, 255, 255)
Black = (0, 0, 0)
White = (255,255,255)
Red = (254,0,0)
Yellow = (255,255,0)

Bullets_speed = 5


Border = pygame.Rect(HEIGHT // 2 - 5, 0, 10, WIDTH)

hello = 0
Space_Ship_Height, Space_Ship_Width = 55, 40
move_speed = 3

Background_Image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")),(HEIGHT,WIDTH))

Yellow_Ship_Image = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
Yellow_Ship = pygame.transform.rotate(pygame.transform.scale(Yellow_Ship_Image, (Space_Ship_Height, Space_Ship_Width)),  90)
#Ship_Pixel_Off = 55
Red_Ship_Image = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
Red_Ship = pygame.transform.rotate(pygame.transform.scale(Red_Ship_Image, (Space_Ship_Height, Space_Ship_Width)), 270)




def draw_window(yellow, red, yellow_bullet, red_bullet, Red_health, Yellow_health,yellow_bullet_count,red_bullet_count,Y_won,R_won):
  
    WIN.blit(Background_Image,(0,0))
    pygame.draw.rect(WIN, Black, Border)
    
    bullet_text_yellow = Health_font.render("Bullets used: "+str(yellow_bullet_count),1,White)
    red_text_yellow = Health_font.render("Bullets used: "+str(red_bullet_count),1,White)
    Red_health_text = Health_font.render("Health: "+str(Red_health),1,White)
    Yellow_health_text = Health_font.render("Health:"+ str(Yellow_health) ,1,White)

    #TODO correctly blit it
    Yellow_won = Health_font.render("Yellow Won:"+str(Y_won),1,White)
    #Red_won = Health_font.render("Red Won:"+str(R_Won),1,White)

    WIN.blit(Red_health_text,(HEIGHT-Red_health_text.get_width()-10,10))

    WIN.blit(Yellow_won,(10,57))

    WIN.blit(bullet_text_yellow,(10,35))
    WIN.blit(red_text_yellow,(HEIGHT-red_text_yellow.get_width()-10,35))

    WIN.blit(Yellow_health_text,(10, 10))

    WIN.blit(Yellow_Ship, (yellow.x, yellow.y))
    WIN.blit(Red_Ship, (red.x, red.y))
    for bullet in yellow_bullet:
        pygame.draw.rect(WIN,Yellow,bullet)
    for bullet in red_bullet:
        pygame.draw.rect(WIN,Red,bullet)

    pygame.display.update()



def yellow_ship_movement(key_pressed, yellow_ship):
    if key_pressed[K_s] and yellow_ship.y < 445:
        yellow_ship.y += move_speed
    elif key_pressed[K_w] and yellow_ship.y > 5:
        yellow_ship.y -= move_speed
    if key_pressed[K_d] and yellow_ship.x < 403:
        yellow_ship.x += move_speed
    elif key_pressed[K_a] and yellow_ship.x > 0:
        yellow_ship.x -= move_speed


def red_ship_movement(key_pressed, red_ship):
    if key_pressed[K_DOWN] and red_ship.y < 445:
        red_ship.y += move_speed
    elif key_pressed[K_UP] and red_ship.y > 5:
        red_ship.y -= move_speed
    if key_pressed[K_RIGHT] and red_ship.x <  861:
        red_ship.x += move_speed
    elif key_pressed[K_LEFT] and red_ship.x > 456:
        red_ship.x -= move_speed


def handle_bullets(Yelllow_Bullets,Red_Bullets,yellow,red):

    for bullet in Yelllow_Bullets:
        bullet.x += Bullets_speed

        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            Yelllow_Bullets.remove(bullet)
        elif bullet.x > HEIGHT:
            Yelllow_Bullets.remove(bullet)
        
        for bullet_red in Red_Bullets:
            if bullet.colliderect(bullet_red):
                Yelllow_Bullets.remove(bullet)
                Red_Bullets.remove(bullet_red)
                hit_sound.play()
    for bullet in Red_Bullets:
        bullet.x -= Bullets_speed
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            Red_Bullets.remove(bullet)
        elif bullet.x < 0:
            Red_Bullets.remove(bullet)   
         

def show_winner(winner):
    
    Winner_text = Winner_font.render(winner,1,White)
    Bottom_text = Winner_font2.render("Game is restarting....",1,White)
    WIN.blit(Winner_text,(HEIGHT/2-Winner_text.get_width()/2,WIDTH/2-Winner_text.get_width()/2+100))
    pygame.display.update()
    pygame.time.delay(2000)    
    WIN.blit(Bottom_text,(HEIGHT/2-Winner_text.get_width()/2+120,WIDTH/2-Winner_text.get_width()/2+240))
    pygame.display.update()
    pygame.time.delay(3000)    



def main():


    Red_win = 0
    Yellow_win = 0

    bullet_used_red = 0
    bullet_used_yellow = 0

    #TODO add win count
    Yelllow_Bullets = []
    Red_Bullets = []
    Max_Bullet = 5

    #00FF00
    yellow = pygame.Rect(50, 50, Space_Ship_Height, Space_Ship_Width)
    red = pygame.Rect(800, 50, Space_Ship_Height, Space_Ship_Width)

    Red_Health = 5
    Yellow_Helth = 5

    clock = pygame.time.Clock()
    run = True



    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SLASH and len(Red_Bullets) != Max_Bullet:
                    bullet_used_red += 1
                    bullet = pygame.Rect(red.x + red.width-60,red.y + red.width // 2 -4 -1, 10, 5)
                    Red_Bullets.append(bullet)
                    Shoot_sound.play()

                if event.key == pygame.K_e and len(Yelllow_Bullets) != Max_Bullet:
                    bullet_used_yellow += 1
                    bullet = pygame.Rect(yellow.x + yellow.width,yellow.y + yellow.width // 2 -5 , 10, 5)
                    Yelllow_Bullets.append(bullet)
                    Shoot_sound.play()
            if event.type == red_hit:
                Red_Health -= 1
                hit_sound.play()
            if event.type == yellow_hit:
                Yellow_Helth -= 1
                hit_sound.play()

        winner = ""
        if Red_Health <= 0:
            winner = "Yellow won!"
            Yellow_win += 1
            show_winner(winner)
            break

    
        if Yellow_Helth <= 0:
            winner = "Red Won!"
            Red_win += 1
            show_winner(winner)
            break
 


        key_pressed = pygame.key.get_pressed()
        yellow_ship_movement(key_pressed, yellow)
        handle_bullets(Yelllow_Bullets,Red_Bullets,yellow,red)
        red_ship_movement(key_pressed, red)
        draw_window(yellow, red, Yelllow_Bullets,Red_Bullets, Red_Health,Yellow_Helth,bullet_used_yellow,bullet_used_red,Yellow_win,Red_win)
    main()


if __name__ == "__main__":
    main()