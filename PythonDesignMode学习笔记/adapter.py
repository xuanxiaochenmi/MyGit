from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def pay(self, money):
        print('支付宝支付%d元' % money)

class WechatPay(Payment):
    def pay(self, money):
        print('微信支付%d元' % money)
        
class BankPay:
    def cost(self,money):
        print('银联支付%d元.'%money)


class ApplePay:
    def cost(self, money):
        print('苹果支付%d元' % money)
# class newBankPay(Payment,BankPay):
#     def pay(self, money):
#         self.cost(money)
#         print('银联支付%d元.'%money)
        
class Adapter(Payment):
    def __init__(self, payment):
        self.payment = payment
        
    def pay(self, money):
        self.payment.cost(money)


p = Adapter(ApplePay())
p.pay(100)
