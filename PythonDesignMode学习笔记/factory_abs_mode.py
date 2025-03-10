from abc import ABCMeta, abstractmethod

# ----抽象产品-----

class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass
class Cpu(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# ----抽象工厂-----

class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_shell(self):
        pass
    @abstractmethod
    def create_cpu(self):
        pass
    @abstractmethod
    def create_os(self):
        pass

# ----具体产品-----

class SmallShell(PhoneShell):
    def show_shell(self):
        print('普通手机小手机壳')
    
class BigShell(PhoneShell):
    def show_shell(self):
        print('普通手机大手机壳')

class AppleShell(PhoneShell):
    def show_shell(self):
        print('苹果手机壳')

class SnapDragonCPU(Cpu):
    def __init__(self,is_64bit=False):
        self.is_64bit = is_64bit
    def show_cpu(self):
        if self.is_64bit:
            print('64位CPU')
        else:
            print('骁龙CPU')
class MediaTekCPU(Cpu):
    def show_cpu(self):
        print('联发科CPU')

class AppleCPU(Cpu):
    def show_cpu(self):
        print('苹果CPU')

class AndroidOS(OS):
    def show_os(self):
        print('安卓系统')

class IOS(OS):
    def show_os(self):
        print('苹果系统')

# ----具体工厂-----

class MiFactory(PhoneFactory):
    def create_shell(self):
        return SmallShell()
    def create_cpu(self):
        return SnapDragonCPU()
    def create_os(self):
        return AndroidOS()

class HuaweiFactory(PhoneFactory):
    def create_shell(self):
        return BigShell()
    def create_cpu(self):
        return MediaTekCPU()
    def create_os(self):
        return AndroidOS()

class AppleFactory(PhoneFactory):
    def create_shell(self):
        return AppleShell()
    def create_cpu(self):
        return AppleCPU()
    def create_os(self):
        return IOS()


# -----client-----

class Phone:
    def __init__(self,shell,cpu,os):
        self.shell = shell
        self.cpu = cpu
        self.os = os
    def show_info(self):
        print('手机信息：')
        self.shell.show_shell()
        self.cpu.show_cpu()
        self.os.show_os()

def make_phone(factory):
    shell = factory.create_shell()
    cpu = factory.create_cpu()
    os = factory.create_os()
    return Phone(shell,cpu,os)

p1 = make_phone(MiFactory())
p1.show_info()
print()
p2 = make_phone(HuaweiFactory())
p2.show_info()
print()
p3  = make_phone(AppleFactory())
p3.show_info()