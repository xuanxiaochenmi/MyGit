from abc import ABCMeta, abstractmethod

# class Payment(metaclass=ABCMeta):
#     @abstractmethod
#     def pay(self, money):
#         pass

# class Alipay(Payment):
#     def pay(self, money):
#         print('支付宝支付%d元' % money)

# class WechatPay(Payment):
#     def pay(self, money):
#         print('微信支付%d元' % money)

# p = Alipay()
# p.pay(200)

# q = WechatPay()
# q.pay(300)

# class User:
#     def __init__(self, name):
#         self.name = name
#     def show_name(self):
#         print(f'用户的名字是{self.name}')
# class VIPUser(User):
#     def __init__(self, name):
#         super().__init__(name) 
#     def show_name(self):
#         print(f'究极牛逼VIP用户的名字是{self.name}')

# def print_name(u):
#     u.show_name()

# print_name(User('小明'))
# print_name(VIPUser('小王'))

class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass

class WaterAnimal(metaclass=ABCMeta):    
    @abstractmethod
    def swin(self):
        pass
class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Tiger(LandAnimal):
    def walk(self):
        print('老虎在跑')

class Frog(LandAnimal,WaterAnimal):
    def walk(self):
        print('青蛙在跳')
    def swin(self):
        print('青蛙在游')

class Goose(LandAnimal, WaterAnimal , SkyAnimal):
    def walk(self):
        print('鹅在跑')
    
    def swin(self):
        print('鹅在游')
    
    def fly(self):
        print('鹅在飞')


t = Tiger()
t.walk()

f = Frog()
f.swin()
f.walk()