from abc import ABCMeta, abstractmethod

class Player:
    def __init__(self,face=None , body=None ,arm=None , leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg
    def __str__(self): #作用：
        return  'face:%s,body:%s,arm:%s,leg:%s' % (self.face,self.body,self.arm,self.leg) 

class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass
    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass
    @abstractmethod
    def build_leg(self):
        pass

class GirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()
    def build_face(self):
        self.player.face = '漂亮脸蛋'
    def build_body(self):
        self.player.body = '苗条'
    def build_arm(self):
        self.player.arm = '长胳膊'
    def build_leg(self):
        self.player.leg = '短腿'

class Moster(PlayerBuilder):
    def __init__(self):
        self.player = Player()
    def build_face(self):
        self.player.face = '丑陋'
    def build_body(self):
        self.player.body = '强壮'
    def build_arm(self):
        self.player.arm = '粗壮'
    def build_leg(self):
        self.player.leg = '短腿'

# 控制组装顺序

class PlayerDirector:

    def build_player(self,builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player
    
# client

builder = GirlBuilder()
director = PlayerDirector()
player = director.build_player(builder)
print(player)