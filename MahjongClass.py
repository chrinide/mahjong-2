# -*- coding:gb2312 -*- #
# Created 2012-3-7
__metaclass__ = type
import re
#Mahjong Class

class Tile:
    def __init__(self,Mname="",Mvalue=0):
        self.Mname = Mname
        self.Mvalue = Mvalue
    def MyName(self):
        print self.Mname
    def MyValue(self):
        print self.Mvalue

class Character(Tile):
    def __init__(self,Mname="",Mvalue=0):
        super(Character,self).__init__(Mname,Mvalue)
  
class Dot(Tile):
    def __init__(self,Mname="",Mvalue=0):
        super(Dot,self).__init__(Mname,Mvalue)
        
class Bamboo(Tile):
    def __init__(self,Mname="",Mvalue=0):
        super(Bamboo,self).__init__(Mname,Mvalue)
        

class Dragon(Tile):
    def __init__(self,Mname="",Mvalue=0):
        super(Dragon,self).__init__(Mname,Mvalue)
        

class Wind(Tile):
    def __init__(self,Mname="",Mvalue=0):
        super(Wind,self).__init__(Mname,Mvalue)
        

class Flower(Tile):
    def __init__(self,Mname="",Mvalue=0):
        super(Flower,self).__init__(Mname,Mvalue)


class BaseComb:
    '''Triplet Sequence Trump Kong的基类，Sequence的Value为其中间的数  '''
    def __init__(self,bvalue = 0):
        self.bvalue = bvalue

class Triplet(BaseComb):
    def __init__(self,bValue=0,isPong=True):
        super(Triplet,self).__init__(bValue)
        self.isPong = isPong

class Sequence(BaseComb):
    def __init__(self,bValue=0,isChow=True):
        super(Sequence,self).__init__(bValue)
        self.isChow = isChow

class Trump(BaseComb):
    def __init__(self,bValue=0):
        super(Trump,self).__init__(bValue)

class Kong(BaseComb):
    def __init__(self,bValue=0,isExposed=True):
        super(Kong,self).__init__(bValue)
        self.isExposed = isExposed

class HandTiles:
    def __init__(self,tiles):
        self.tiles = tiles[:]
        self.drawSelf = False
        self.tilePoints = ""
    
    def getPoints(self):
        return self.tilePoints
    
        
dictMTile = {0:'1C',1:'2C',2:'3C',3:'4C',4:'5C',5:'6C',6:'7C',7:'8C',8:'9C',
         10:'1D',11:'2D',12:'3D',13:'4D',14:'5D',15:'6D',16:'7D',17:'8D',18:'9D',
         20:'1B',21:'2B',22:'3B',23:'4B',24:'5B',25:'6B',26:'7B',27:'8B',28:'9B',
         30:'EW',31:'SW',32:'WW',33:'NW',34:'RD',35:'GD',36:'WD',
         40:'SP',41:'SU',42:'AU',43:'WI',44:'PL',45:'OR',46:'BA',47:'CH',}

dictPoints = {'SIFENGHUI':'四风会'}
SiFengHui = re.compile('\d{28}')



if __name__ == '__main__':

    randtile00 = [30,30,30,31,31,31,32,32,32,33,33,33,35,35]
    randtile49 = [7,7,7,17,17,17,27,27,27,36,36,36,30,30]
    randtile48 = [1,2,3,12,13,14,23,24,25,26,26,26,13,13]

    b = []
    

    
     
