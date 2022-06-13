__author__ = 'linkmanap123'
from Player import Player
from NPC import NPC
from Map import Map
import graphics
import json
import pygame
import math
import os
import random
import operator
import intersects
import time
from spritesheet import spritesheet

# Set window position
os.environ['SDL_VIDEO_WINDOW_POS'] = "200,30:"


# Initialize game engine
pygame.init()


# Window
width = 1200
height = 750
SIZE = (width, height)
TITLE = "RPG"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)
myfont = pygame.font.SysFont("monospace", 50)

# Timer
clock = pygame.time.Clock()
refresh_rate = 35

'''SPRITE SHEET LOADDDDDDDDDDDDDDDD'''
sprite_sheet = spritesheet("img/map/basictiles.png")

#Health Max, Attack, Special, Heal, Current Health, Spc Num, Spc Max, level, current xp, xp2level
#name = input("ENTER YOUR NAME: ")
save_load = []
with open("json/save.json") as n:
    save = n.read()
save_load = json.loads(save)
print(save_load)
for i in save_load:
    if 'saved' in i:
        if 'saved' in i:
            if i['saved'] == "True":
                if 'name' in i:
                    name = i['name']
                if 'health_max' in i:
                    health_max = i['health_max']
                if 'health' in i:
                    health = i['health']
                if 'attack' in i:
                    attack = i['attack']
                if 'heal' in i:
                    heal = i['heal']
                if 'sp_num' in i:
                    sp_num = i['sp_num']
                if 'sp_max' in i:
                    sp_max = i['sp_max']
                if 'level' in i:
                    level = i['level']
                if 'xp' in i:
                    xp = i['xp']
                if 'xp_to_level' in i:
                    xp2lvl = i['xp_to_level']

                player = Player(name,health_max,attack,heal,health,sp_num,sp_max,level,xp,xp2lvl)
            else:
                name = graphics.name_entry()
                player = Player(name, 10, 3, 2, 10, 3, 3, 1, 0, 10)





with open ('json/npc1.json') as n:
   npclist = n.read()
record_set = []
record_set = json.loads(npclist)
npc_list = []
dead_list = []
dead_list_serial = []
with open ('json/map1_1.json') as n:
   maplist = n.read()
map_set = []
map_set = json.loads(maplist)
map_list = []


a = ["Lets Fight!", "Good Fight!"]

b = ['The Triforce parts are resonating. ','They are combining into one again.'
     'The two parts that I could not ', 'capture on that day seven years ago...'
     "I didn't expect that they would",'be hidden within you two. These toys are '
     'too much for you!', '',
     'I demand you return them to me.'
     ]

for i in record_set:
    if 'x' in i:
        x = i['x']
    if 'y' in i:
        y = i['y']
    if 'type' in i:
        type = i['type']
    if 'health' in i:
        health = i['health']
    if 'attack' in i:
        attack = i['attack']
    if 'xp' in i:
        xp = i['xp']
    if 'serial' in i:
        serial = i['serial']
    #we'll do text but i got to ask the coop ;)
    #till then we're loading in sample texts
    if 'file_loc' in i:
        file = i['file_loc']

    npc_list.append(NPC(x,y,type,health,attack,xp,a,file,serial))


'''Things that the MAP objects take in and are used for loading in from sprite sheet'''
for i in map_set:
    if 'x' in i:
        x = i['x']
    if 'y' in i:
        y = i['y']
    if 'type' in i:
        type = i['type']
    if 'file_x' in i:
        file_x = i['file_x']
    if 'file_y' in i:
        file_y = i['file_y']
    if 'width' in i:
        width = i['width']
    if 'height' in i:
        height = i['height']
    if 'map_lead_to' in i:
        map_lead_to = i['map_lead_to']
    else:
        map_lead_to = 'none'
    if 'npc_lead_to' in i:
        npc_lead_to = i['npc_lead_to']
    else:
        npc_lead_to = 'none'
    map_list.append(Map(x,y,type,file_x,file_y,width,height,map_lead_to,npc_lead_to))


#for i in map_list:
#    if i.type == "background":
 #       background = pygame.image.load(os.path.join(i.file_loc))
#colors
WHITE = (255,255,255)

player_loc = [490, 590]
#quick load
quick_load = 0
level_num = 1

# Game loop
done = False
while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player_loc[1] -= 5
    if key[pygame.K_s]:
        player_loc[1] += 5
    if key[pygame.K_d]:
        player_loc[0] += 5
    if key[pygame.K_a]:
        player_loc[0] -= 5



    '''Collision Detection'''
    player_rect = [player_loc[0], player_loc[1], 90, 90]
    for i in npc_list:
        if i.serial not in dead_list_serial:
            npc_rect = [i.x, i.y, 40, 40]
        if intersects.rect_rect(player_rect, npc_rect):
            if i.type == "enemy":
                e_max = i.health
                while i.health > 0 and player.health > 0:
                    choice = graphics.battle_draw(player.health, player.health_max, player.sp_num,player.sp_max,player.xp,player.xp_to_level,i.health,e_max)
                    i.health = player.fight(choice, i.type, i.health, i.attack, i.text)
                    e_move = player.get_emove()
                    graphics.battle_effect(e_move,choice)
                    if i.health <= 0:
                        npc_list.remove(i)
                        player.xp += i.xp
                        dead_list.append(i)
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        player.talk(i.type, i.text)
    for i in map_list:
        map_rect  = [i.x, i.y, i.width, i.height]
        if intersects.rect_rect(player_rect, map_rect):
            if i.type == "wall":
                player_loc = old_loc



    '''LOADING LEVELS'''
    for m in map_list:
        map_rect  = [m.x, m.y, m.width, m.height]
        if intersects.rect_rect(player_rect, map_rect):
            if m.type == "door_center" or m.type == "door_left" or m.type == "door_right" or m.type == "door_up" or m.type == "door_down":

                npc_file_name = m.npc_file_lead
                print(npc_file_name)
                with open (npc_file_name) as n:
                    npclist = n.read()
                record_set = []
                record_set = json.loads(npclist)
                npc_list.clear()
                for i in record_set:
                    if 'x' in i:
                        x = i['x']
                    if 'y' in i:
                        y = i['y']
                    if 'type' in i:
                        type = i['type']
                    if 'health' in i:
                        health = i['health']
                    if 'attack' in i:
                        attack = i['attack']
                    if 'xp' in i:
                        xp = i['xp']
                    if 'serial' in i:
                        serial = i['serial']
                    #we'll do text but i got to ask the coop ;)
                    #till then we're loading in sample texts
                    if 'file_loc' in i:
                        file = i['file_loc']

                    npc_list.append(NPC(x,y,type,health,attack,xp,b,file,serial))

                map_file_name = m.map_file_lead
                with open (map_file_name) as n:
                    maplist = n.read()
                map_set = []
                map_set = json.loads(maplist)
                map_list.clear()
                for i in map_set:
                    if 'x' in i:
                        x = i['x']
                    if 'y' in i:
                        y = i['y']
                    if 'type' in i:
                        type = i['type']
                    if 'file_x' in i:
                        file_x = i['file_x']
                    if 'file_y' in i:
                        file_y = i['file_y']
                    if 'width' in i:
                        width = i['width']
                    if 'height' in i:
                        height = i['height']
                    if 'map_lead_to' in i:
                        map_lead_to = i['map_lead_to']
                    else:
                        map_lead_to = 'none'
                    if 'npc_lead_to' in i:
                        npc_lead_to = i['npc_lead_to']
                    else:
                        npc_lead_to = 'none'
                    map_list.append(Map(x,y,type,file_x,file_y,map_lead_to,npc_lead_to))
                for i in map_list:
                    if i.type == "background":
                        background = pygame.image.load(os.path.join(i.file_loc))
                if m.type == "door_right":
                    player_loc[0] = 60
                elif m.type == "door_left":
                    player_loc[0] = width-100
                elif m.type == "door_up":
                    player_loc[1] = height - 100
                elif m.type == "door_down":
                    player_loc[1] = 60
                elif m.type == "door_center":
                    player_loc = old_loc





    '''END GAME CHECKS'''
    lvl_count = 0
    if player.health <= 0:
        print("GAME OVER!")
        done = True
    if player.xp >= player.xp_to_level:
        while lvl_count != 2:
            choice = graphics.level_up_draw()
            player.level_up(choice)
            lvl_count += 1

    old_loc = [player_loc[0], player_loc[1]]


    '''********************'''
    '''      DRAWING       '''
    '''********************'''
    screen.fill((255,255,0))
    #ALWAYS ON TOP BBY
    #screen.blit(background, (0,0))
    #screen.fill((76,153,0))
    #Loading in files

    for i in dead_list:
        dead_list_serial.append(i.serial)


    if quick_load == 0:
        for i in npc_list:
            if i.serial not in dead_list_serial:
                npc_draw = pygame.image.load(os.path.join(i.file_loc))
                screen.blit(npc_draw, (i.x,i.y))
    if quick_load == 0:
        for i in map_list:
            if i.type != "background":
                '''*********************************'''
                '''SPRITE SHEETS ARE MY  THING      '''
                '''*********************************'''
                image = sprite_sheet.image_at([int(i.file_x),int(i.file_y),int(i.width),int(i.height)],(0,0,0,0))
                #map_draw = pygame.image.load(os.path.join(i.file_loc))
                screen.blit(image, (i.x,i.y))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                prompt = myfont.render("SAVING", 1, (WHITE))
                screen.blit(prompt, (500, 300))
                pygame.display.flip()
                clock.tick(refresh_rate)
                time.sleep(1)
                player.save(save_load)




    pygame.draw.rect(screen, (0,0,0), [player_loc[0], player_loc[1], 16, 16])


    #Drawing NPCs
    #for i in npc_list:
        #pygame.draw.rect(screen, WHITE, [i.x, i.y, 20, 20])




    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window on quit
pygame.quit()


