__author__ = 'linkmanap123'

class NPC():

    def __init__(self,x, y, type, hp, atk, xp, txt, file_loc, serial):

        self.x = x
        self.y = y
        self.type = type
        self.health = hp
        self.attack = atk
        self.xp = xp
        self.text = txt
        self.file_loc = file_loc
        self.serial = serial