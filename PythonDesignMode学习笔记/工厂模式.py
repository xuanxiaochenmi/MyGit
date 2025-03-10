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
class PayFactory:
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechatpay':
            return WechatPay()
        else:
            return TypeError('Error')

#client
pf = PayFactory()
p = pf.create_payment('alipay')
p.pay(100)
