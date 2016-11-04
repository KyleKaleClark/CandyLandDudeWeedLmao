__author__ = 'linkmanap123'
import random
import time
import json
import graphics
import pygame
e_move = 0
class Player():

    def __init__(self, name, MHealth, Atk, Heal, Health, SPNum, SPMax, level, xp, Xp2lvl):

        self.name = name
        self.health_max = MHealth
        self.attack = Atk
        self.special = self.attack*1.75
        self.heal = Heal
        self.health = Health
        self.sp_num = SPNum
        self.sp_max = SPMax
        self.level = level
        self.xp = xp
        self.xp_to_level = Xp2lvl

    def level_up(self, lvl_choice):

        print("YOU CAN UPGRADE 2 STATS")

        if lvl_choice == 1:
            self.health_max += 5
            self.health = self.health_max

        elif lvl_choice == 2:
            self.attack += 2
            self.special = self.attack*2

        elif lvl_choice == 3:
            self.sp_max += 1
            self.sp_num = self.sp_max

        elif lvl_choice == 4:
            self.heal += 3

        else:
            print("dude thats not an option :| ")

        self.xp_to_level *= 1.5
        self.xp = 0
        self.level += 1
        print("Health:", self.health_max, " Attack: ", self.attack, " Special: ", self.special, " Special Usage: ", self.sp_max,
              " Heal: ", self.heal)

    '''NPC INTERACTION'''
    def talk(self, type, text_list):
        if (type == "npc"):
            loop_count = 1
            for i in text_list:
                print(i)

                if loop_count%2 == 0:
                    time.sleep(2)
                loop_count += 1
    def get_emove(self):
        return e_move
    def fight(self, choice, type, e_health, e_atk, e_txt):
        global e_move
        if type == "enemy":
            if e_health >= 1 and self.health >= 1:
                e_move = random.randint(1,2)
                if choice == 1:
                    if e_move == 2:
                        #animations
                        print("HE BLOCKED")
                        self.health -= e_atk * .3
                    else:
                        e_health -= self.attack

                elif choice == 3:
                    if self.sp_num > 0:
                        if e_move == 2:
                            #animations
                            print("HE BLOCKED")
                            self.health -= e_atk * .3
                            self.sp_num -= 1
                        else:
                            #animations
                            e_health -= self.special
                            self.sp_num -= 1
                    else:
                        print("NO MORE SPECIAL")

                elif choice == 4:
                    if self.health < self.health_max:
                        self.health += self.heal
                        if self.health >= self.health_max:
                            self.health = self.health_max
                        #animations
                    else:
                        print("HEALTH MAXED")

                #enemy turn

                elif choice == 2:
                    if e_move == 2:
                        print("BOTH BLOCKED")
                        #animations
                    elif e_move == 1:
                        print("BLOCKED HIS MOVE")
                        e_health -= self.attack *.3
                        #animations

                elif choice == 5:
                    e_move = 3


                if e_move == 1:
                    if choice == 2:
                        print("BLOCKED HIS MOVE")
                    elif choice == 1 or choice == 3 or choice == 4:
                        print("HE HIT YOU")
                        self.health -= e_atk


                #Status
                print("Health ", self.health)
                print("e_health ", e_health)
                if self.health < 1:
                    self.health = 0
                return e_health
            else:
                return 0
        else:
            print("Not an Enemy")

    def save(self, save_load):
        for i in save_load:
            for key in i.keys():
                if key == 'saved':
                    i['saved'] = "True"
                if key == 'health_max':
                    i['health_max'] = self.health_max
                if key == 'heal':
                    i['heal'] = self.heal
                if key == 'sp_max':
                    i['sp_max'] = self.sp_max
                if key == 'sp_num':
                    i['sp_num'] = self.sp_num
                if key == 'attack':
                    i['attack'] = self.attack
                if key == 'xp':
                    i['xp'] = self.xp
                if key == 'level':
                    i['level'] = self.level
                if key == 'xp_to_level':
                    i['xp_to_level'] = self.xp_to_level
                if key == 'name':
                    i['name'] = self.name
                if key == 'health':
                    i['health'] = self.health
                #do this for all of tyhem and set them to self.whateverd
        pretty_json_string = json.dumps(save_load, indent=4)
        with open ('json/save.json','w') as s:
            s.write(pretty_json_string)




























