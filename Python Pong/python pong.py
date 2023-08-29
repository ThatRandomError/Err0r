import pygame
from sys import exit

pygame.init()
## vars
score_player1 = 0
score_player2 = 0

ball_x = 850
ball_y = 600

ball_vel_x = 5
ball_vel_y = 5

title_screen = 1

game_won = 0

screen = pygame.display.set_mode((1900,1200))
pygame.display.set_caption("Pyong")
clock = pygame.time.Clock()

background = pygame.Surface((1900,1200))

player1 = pygame.Surface((20,270))
player1.fill("White")
player1_rect = player1.get_rect(topleft = (20,200))

player2 = pygame.Surface((20,270))
player2.fill("White")
player2_rect = player2.get_rect(topleft = (1860,200))

ball = pygame.Surface((20,20))
ball_rect = ball.get_rect(topleft = (ball_x,ball_y))
ball.fill("White")

button = pygame.Surface((500,200))
button_rect = button.get_rect(topleft = (700,545))
button.fill("White")

bottom_text = pygame.font.Font("font/PixelFont.ttf", 50)
bottom_t_suf = bottom_text.render("Press Start Or Space", False, "White")

won_text1 = bottom_text.render("Player 1 Won",False,"White")
won_text2 = bottom_text.render("Player 2 Won",False,"White")

button_text = pygame.font.Font("font/PixelFont.ttf", 90)
button_t_suf = button_text.render("Start" , False, "Black")

title = pygame.font.Font("font/PixelFont.ttf", 100)
title_suf = title.render("PONG", False, "White")

score1 = pygame.font.Font("font/PixelFont.ttf", 100)
score2 = pygame.font.Font("font/PixelFont.ttf", 100)

underline = pygame.Surface((1860, 20))
underline.fill("White")

score1_suf_0 = score1.render("0", False, "White")
score2_suf_0 = score1.render("0", False, "White")

score1_suf_1 = score1.render("1", False, "White")
score2_suf_1 = score1.render("1", False, "White")

score1_suf_2 = score1.render("2", False, "White")
score2_suf_2 = score1.render("2", False, "White")

score1_suf_3 = score1.render("3", False, "White")
score2_suf_3 = score1.render("3", False, "White")

score1_suf_4 = score1.render("4", False, "White")
score2_suf_4 = score1.render("4", False, "White")

score1_suf_5 = score1.render("5", False, "White")
score2_suf_5 = score1.render("5", False, "White")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if (event.type == pygame.KEYDOWN):
            if (player1_rect.y != 200):
                if (event.key==pygame.K_w):
                    player1_rect.y -= 45
            if (player1_rect.y != 920):
                if (event.key==pygame.K_s):
                    player1_rect.y += 45
            if (player2_rect.y != 200):
                if (event.key==pygame.K_i):
                    player2_rect.y -= 45
            if (player2_rect.y != 920):
                if (event.key==pygame.K_k):
                    player2_rect.y += 45
            if (event.key==pygame.K_SPACE):
                title_screen = 0
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (button_rect.collidepoint(event.pos)):
                title_screen = 0


    screen.blit(background,(0,0))
    screen.blit(title_suf,(750,5))
    screen.blit(underline,(20,150))
    ##game running
    if (title_screen == 0 ):
        game_won = 0
        screen.blit(player1,player1_rect)
        screen.blit(player2,player2_rect)
        screen.blit(ball,ball_rect)

        if(score_player1 == 0):
            screen.blit(score1_suf_0,(20,20))
        if(score_player2 == 0):
            screen.blit(score2_suf_0,(1790,20))

        if(score_player1 == 1):
            screen.blit(score1_suf_1,(20,20))
        if(score_player2 == 1):
            screen.blit(score2_suf_1,(1790,20))

        if(score_player1 == 2):
            screen.blit(score1_suf_2,(20,20))
        if(score_player2 == 2):
            screen.blit(score2_suf_2,(1790,20))

        if(score_player1 == 3):
            screen.blit(score1_suf_3,(20,20))
        if(score_player2 == 3):
            screen.blit(score2_suf_3,(1790,20))

        if(score_player1 == 4):
            screen.blit(score1_suf_4,(20,20))
        if(score_player2 == 4):
            screen.blit(score2_suf_4,(1790,20))

        if(score_player1 == 5):
            screen.blit(score1_suf_5,(20,20))
            title_screen = 1
            game_won = 1
        if(score_player2 == 5):
            screen.blit(score2_suf_5,(1790,20))
            title_screen = 1
            game_won = 2
            
        ball_rect.x += ball_vel_x
        ball_rect.y += ball_vel_y
        if (player1_rect.colliderect(ball_rect) == 1):
            ball_vel_x *= -1
        if (player2_rect.colliderect(ball_rect) == 1):
            ball_vel_x *= -1
        if (ball_rect.top <= 170 or ball_rect.bottom >= 1200):
            ball_vel_y *= -1
        if (ball_rect.left <= 0):
            score_player2 += 1
            ball_rect.x = 850
            ball_rect.y = 600
        if (ball_rect.right >= 1900):
            score_player1 += 1
            ball_rect.x = 850
            ball_rect.y = 600
    else:
        score_player1 = 0
        score_player2 = 0
        if (game_won==1):
            screen.blit(won_text1, (620, 1000))
        if (game_won==2):
            screen.blit(won_text1, (620, 1000))

        screen.blit(button, button_rect)

        screen.blit(button_t_suf, (730,590))
        screen.blit(bottom_t_suf, (450, 1100))
    pygame.display.update()
    clock.tick(60)