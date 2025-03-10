from abc import ABCMeta ,abstractmethod
class Singleton:
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
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
