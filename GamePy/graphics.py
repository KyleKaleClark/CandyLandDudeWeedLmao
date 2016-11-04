__author__ = 'linkmanap123'

import pygame
import os
import time

SIZE = (960, 600)
TITLE = "RPG"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont("monospace", 50)
myfont2 = pygame.font.SysFont("monospace", 25)
myfont3 = pygame.font.SysFont("monospace", 30)

WHITE = (255,255,255)
GREY = (100,100,100)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
e_health_bar = pygame.image.load(os.path.join("img/battle/e_bar.png"))
enemy_img = pygame.image.load(os.path.join("img/battle/enemy.png"))
player_img = pygame.image.load(os.path.join("img/battle/player.png"))
pointer = pygame.image.load(os.path.join("img/battle/pointer.png"))
status_bar = pygame.image.load(os.path.join("img/battle/status_bar.png"))
confetti = pygame.image.load(os.path.join("img/battle/confetti.png"))
x = 100
y = 500
choice = 1
done = False
refresh_rate = 30
d = 1
length = 360


def name_entry():
    name_list = []
    name_string = ""
    while 2 == 2:
        screen.fill(GREY)
        pygame.draw.rect(screen, BLACK, (50,475,1000, 100))
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and len(name_list) != 30:
                    if event.key == pygame.K_a:
                        name_list.append("a")
                    elif event.key == pygame.K_b:
                        name_list.append("b")
                    elif event.key == pygame.K_c:
                        name_list.append("c")
                    elif event.key == pygame.K_d:
                        name_list.append("d")
                    elif event.key == pygame.K_e:
                        name_list.append("e")
                    elif event.key == pygame.K_f:
                        name_list.append("f")
                    elif event.key == pygame.K_g:
                        name_list.append("g")
                    elif event.key == pygame.K_h:
                        name_list.append("h")
                    elif event.key == pygame.K_i:
                        name_list.append("i")
                    elif event.key == pygame.K_j:
                        name_list.append("j")
                    elif event.key == pygame.K_k:
                        name_list.append("k")
                    elif event.key == pygame.K_l:
                        name_list.append("l")
                    elif event.key == pygame.K_m:
                        name_list.append("m")
                    elif event.key == pygame.K_n:
                        name_list.append("n")
                    elif event.key == pygame.K_o:
                        name_list.append("o")
                    elif event.key == pygame.K_p:
                        name_list.append("p")
                    elif event.key == pygame.K_q:
                        name_list.append("q")
                    elif event.key == pygame.K_r:
                        name_list.append("r")
                    elif event.key == pygame.K_s:
                        name_list.append("s")
                    elif event.key == pygame.K_t:
                        name_list.append("t")
                    elif event.key == pygame.K_u:
                        name_list.append("u")
                    elif event.key == pygame.K_v:
                        name_list.append("v")
                    elif event.key == pygame.K_w:
                        name_list.append("w")
                    elif event.key == pygame.K_x:
                        name_list.append("x")
                    elif event.key == pygame.K_y:
                        name_list.append("y")
                    elif event.key == pygame.K_z:
                        name_list.append("z")
                    elif event.key == pygame.K_SPACE:
                        name_list.append(" ")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE and len(name_list) > 0:
                        name_list.pop(-1)

                    elif event.key == pygame.K_RETURN:
                        return name_string
        name_string = "".join(name_list)
        name_render = myfont.render(name_string, 1, (255,255,255))
        screen.blit(name_render, (100,500))
        prompt = myfont.render("ENTER YOUR NAME:", 1, (WHITE))
        screen.blit(prompt, (100, 200))
        pygame.display.flip()
        clock.tick(refresh_rate)

def level_up_draw():
    x = 140
    y = 595
    c_x = 50
    c_y = -2000
    choice = 1
    while 2 == 2:
        screen.fill(BLACK)
        screen.blit(confetti, (c_x, c_y))
        screen.blit(player_img, (500,300))
        pygame.draw.rect(screen, GREY, (50, 500, 1100, 200))
        dialouge = myfont3.render("LEVEL UP! PICK A STAT!", 1, BLACK)
        option = myfont3.render("Health      Attack      Special Usage       Heal", 1, (0,0,0))
        screen.blit(option, (175, 595))
        screen.blit(dialouge, (375, 510))
        screen.blit(pointer, (x, y))

        c_y += 10
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and choice != 2 and choice != 1:
                    choice -= 2
                elif event.key == pygame.K_s and choice != 3 and choice != 4:
                    choice += 2
                elif event.key == pygame.K_a and choice != 1:
                    choice -= 1
                elif event.key == pygame.K_d and choice != 4:
                    choice += 1
                elif event.key == pygame.K_RETURN:
                    return choice

        if choice == 1:
            x = 120
            y = 585
        elif choice == 2:
            x = 330
            y = 585
        elif choice == 3:
            x = 550
            y = 585
        elif choice == 4:
            x = 900
            y = 585

        pygame.display.flip()
        clock.tick(refresh_rate)

def battle_draw(health, health_max, sp_num, sp_max, xp, xp_max, e_health, e_max):
    if e_health >= 0 and health >= 0:
        start_length = 360
        p_hp_start_length = 220
        p_xp_start_length = 220
        global d, done, choice, x, y, length
        length = (e_health*start_length)/e_max
        p_hp_length = (health*p_hp_start_length)/health_max
        p_xp_length = (xp*p_xp_start_length)/xp_max
        screen.fill((255,255,255))

        #Status Bars
        pygame.draw.rect(screen, RED, (142,60,length,50))
        pygame.draw.rect(screen, GREY, (875, 545, 230, 30))
        pygame.draw.rect(screen, BLACK, (880, 550, 220, 20))
        pygame.draw.rect(screen, RED, (880, 550, p_hp_length, 20))

        pygame.draw.rect(screen, GREY, (875, 645, 230, 30))
        pygame.draw.rect(screen, BLACK, (880, 650, 220, 20))
        pygame.draw.rect(screen, BLUE, (880, 650, p_xp_length, 20))


        while d == 1:

            #Behind
            if e_health < 0:
                d = 3


            #Images

            pygame.draw.rect(screen, GREY, (50, 450, 750, 250))
            screen.blit(e_health_bar, (50,50))
            screen.blit(enemy_img, (700,50))
            screen.blit(player_img, (100,250))
            screen.blit(status_bar,(850,450))
            screen.blit(pointer, (x, y))

            #Text
            attack = myfont.render("Attack", 1, (0,0,0))
            screen.blit(attack, (175, 495))
            defense = myfont.render("Defense", 1, (0,0,0))
            screen.blit(defense, (510, 495))
            special = myfont.render("Special", 1, (0,0,0))
            screen.blit(special, (175, 595))
            heal = myfont.render("Heal", 1, (0,0,0))
            screen.blit(heal, (510, 595))
            player_hp = myfont2.render("HP:", 1, (0,0,0))
            screen.blit(player_hp, (875,510))
            player_sp = myfont2.render("SP:", 1, (0,0,0))
            screen.blit(player_sp, (875,580))
            player_xp = myfont2.render("XP:", 1, (0,0,0))
            screen.blit(player_xp, (875,610))
            hp_text = str(int(health))
            hp_text_max = str(int(health_max))
            dash = " / "
            player_hp_out_of = myfont2.render(hp_text, 1, (0,0,0))
            screen.blit(player_hp_out_of, (920, 510))
            player_hp_out_of2 = myfont2.render(dash, 1, (0,0,0))
            screen.blit(player_hp_out_of2, (935, 510))
            player_hp_out_of3 = myfont2.render(hp_text_max, 1, (0,0,0))
            screen.blit(player_hp_out_of3, (965, 510))


            sp_text = str(int(sp_num))
            sp_text_max = str(int(sp_max))
            player_sp_out_of = myfont2.render(sp_text, 1, (0,0,0))
            screen.blit(player_sp_out_of, (920, 580))
            player_sp_out_of2 = myfont2.render(dash, 1, (0,0,0))
            screen.blit(player_sp_out_of2, (935, 580))
            player_sp_out_of3 = myfont2.render(sp_text_max, 1, (0,0,0))
            screen.blit(player_sp_out_of3, (965, 580))

            xp_text = str(int(xp))
            xp_text_max = str(int(xp_max))
            player_xp_out_of = myfont2.render(xp_text, 1, (0,0,0))
            screen.blit(player_xp_out_of, (920, 610))
            player_xp_out_of2 = myfont2.render(dash, 1, (0,0,0))
            screen.blit(player_xp_out_of2, (935, 610))
            player_xp_out_of3 = myfont2.render(xp_text_max, 1, (0,0,0))
            screen.blit(player_xp_out_of3, (965, 610))



            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and choice != 2 and choice != 1:
                        choice -= 2
                    elif event.key == pygame.K_s and choice != 3 and choice != 4:
                        choice += 2
                    elif event.key == pygame.K_a and choice != 1:
                        choice -= 1
                    elif event.key == pygame.K_d and choice != 4:
                        choice += 1
                    elif event.key == pygame.K_RETURN:
                        return choice
                        d = 4
                        print("h")




            #Decision
            if choice == 1:
                x = 100
                y = 500
            elif choice == 2:
                x = 450
                y = 500
            elif choice == 3:
                x = 100
                y = 600
            elif choice == 4:
                x = 450
                y = 600
            elif choice == 5:
                print('?')
            else:
                print('woopsie')


            pygame.display.flip()
            clock.tick(refresh_rate)
    else:
        choice = 5
        return choice


def battle_effect(e_move,p_move):
    start_time = time.time()
    elapsed_time = 0
    while elapsed_time < 1:

        pygame.draw.rect(screen, GREY, (50, 450, 750, 250))
        if e_move == 1:
            pygame.draw.rect(screen, BLACK, (700,100,100,300))
            e_line = myfont.render("Enemy Attacked!", 1, (0,0,0))
        elif e_move == 2:
            pygame.draw.circle(screen, BLACK, (750,200), 120)
            e_line = myfont.render("Enemy Blocked!", 1, (0,0,0))
        if p_move == 1:
            pygame.draw.rect(screen, BLACK, (300,300,50,150))
            p_line = myfont.render("You Attacked!", 1, (0,0,0))
        elif p_move == 2:
            pygame.draw.circle(screen, BLACK, (300,300), 100)
            p_line = myfont.render("You Blocked!", 1, (0,0,0))
        elif p_move == 3:
            pygame.draw.rect(screen, RED, (300,300,50,150))
            p_line = myfont.render("You Used Special", 1, (0,0,0))
        elif p_move == 4:
            pygame.draw.circle(screen, (255,255,0),(300,300), 100)
            p_line = myfont.render("You Healed!", 1, (0,0,0))
        screen.blit(p_line, (150, 500))
        screen.blit(e_line, (150, 575))
        elapsed_time = time.time()-start_time
        pygame.display.flip()
        clock.tick(refresh_rate)

def pause_screen():
    pygame.draw.rect(screen, GREY, (20,20,1160,710))








