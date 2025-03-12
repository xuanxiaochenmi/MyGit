from abc import ABCMeta ,abstractmethod
class Singleton:
    _instance = None
    def __new__(cls,*args,**kwargs):
        # 判断是否有实例，没有实例则创建实例，有实例则直接返回实例
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self,name):
        self.name = name

a = MyClass('a')
b = MyClass('b')

print(a.name)
print(b.name)
print(a is b)
