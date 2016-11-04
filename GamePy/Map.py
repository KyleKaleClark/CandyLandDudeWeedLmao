__author__ = 'linkmanap123'

class Map():

    def __init__(self, x, y, type, file_x, file_y,width,height, map_file_lead=None, npc_file_lead=None):
        self.x = x
        self.y = y
        self.type = type
        self.file_x = file_x
        self.file_y = file_y
        self.width = width
        self.height = height
        self.map_file_lead = map_file_lead
        self.npc_file_lead = npc_file_lead