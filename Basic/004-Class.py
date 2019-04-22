#对象的定义：

#对象：一个对象有自己的状态、行为和唯一的标识；所有相同类型的对象所具有的结构和行为在他们共同的类中被定义。

#状态（state）：包括这个对象已有的属性（通常是类里面已经定义好的）在加上对象具有的当前属性值（这些属性往往是动态的）

#行为（behavior）：是指一个对象如何影响外界及被外界影响，表现为对象自身状态的改变和信息的传递。

#标识（identity）：是指一个对象所具有的区别于所有其它对象的属性。（本质上指内存中所创建的对象的地址）

__metaclass__ = type

class Person:
    def __init__(self, name):  #初始化函数 ，类中定义函数必须第一个参数是self
        self.name = name

    def getName(self):
        return self.name

    def color(self, color):
        print("%s is %s" % (self.name, color))

class NewPerson:
    def __init__(self, name, lang="golang", website="www.google.com"):  #默认值
        self.name = name
        self.lang = lang
        self.website = website
        self.email = "qiwsir@gmail.com"

