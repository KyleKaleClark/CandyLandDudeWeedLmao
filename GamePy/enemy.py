__author__ = 'linkmanap123'
from NPC import NPC

class Enemy(NPC):

    def __init__(self,x, y, type, hp, atk, xp, txt, file_loc, serial) :
        super.__init__(self,x, y, type, hp, atk, xp, txt, file_loc, serial)

    #MIGHT IMPLEMENT A SEPERATE MOVE FUNCTION LATERdw