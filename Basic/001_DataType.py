#! python3
# create by kmm at 2018-08-04
print("===========================================")
print("create by kmm at 2018-08-04")
print()
print("Start to learn python data type session...")
print()
print("Good Luck!!!")
print("===========================================")
print()

#整数3
#长整数333333333333333333333L
#浮点数3.22222
#负数-3
#使用id(3),可以查看对象整数3的"内存地址" --内置函数id()
print("数字3存储的内存地址：" , id(3))
print("数字3.0存储的内存地址：" , id(3.0))
print()
#使用type()内置函数获取：对象的类型
print("数字3存储的数据类型：" , type(3))
print("数字3.0存储的数据类型：" , type(3.0))
print()

#变量
#在Python中，有这样一句话是非常重要的：对象有类型，变量无类型
#当x = 5时，就是将x这个标签拴在了5上了，通过这个x，就顺延看到了5
x = 5
print("变量x的值是：%d" %(x))
print()

#四则运算
#四个运算符号：加(+)、减(-)、乘(*)、除(/)
print("4+2的和是：", 4+2)
print("4.0+2的和是：", 4.0+2)  #自动向精度高的转换
print("4.0+2.0的和是：", 4.0+2.0)
print()

#整数溢出问题
#Python支持**“无限精度”的整数，**一般情况下不用考虑整数溢出的问题，
#而且Python Int类型与任意精度的Long整数类可以无缝转换，超过Int 范围的情况都将转换成Long类型
#注意：前面的“无限精度”是有引号的。事实上也是有限制的，对于32位的机器，其上限是：2^32-1。真的足够大了
print("两个大整数相乘：2899887676637907866*1788778992788348277389943 = ", 2899887676637907866*1788778992788348277389943)
#64位的电脑精度：（2的64次方-1）
#两个整数相乘：阿拉伯乘法  http://ualr.edu/lasmoller/medievalmult.html
print()


#除法
#整数除以整数
#在Python2.x中，整数除以整数，结果是整数（商），简称取整
print("在Python2.x中，2除以5等于", 2//5)
#在Python3.x中，规则又变了，如果1/2，结果就是0.5，也就是说Python3中的除法是真正的除法了，要取整，只能用1//2的方式，即1//2=0
print("在Python3.x中，2除以5等于", 2/5)

#不管是被除数还是除数，只要有一个数是浮点数，结果就是浮点数
print("2除以5.0等于", 2/5.0)
print("2.0除以5等于", 2.0/5)
print("2.0除以5.0等于", 2.0/5.0)
print()

#10.0除以3等于 3.3333333333333335
#十进制和二进制的转换上，computer姑娘用的是二进制进行计算，
#上面的例子中，我们输入的是十进制，她就要把十进制的数转化为二进制，然后再计算。但是，在转化中，浮点数转化为二进制，就出问题了
print("10.0除以3等于", 10.0/3)
#就Python的浮点数运算而言，大多数机器上每次计算误差不超过 2**53 分之一。
#对于大多数任务这已经足够了，但是要在心中记住这不是十进制算法，每个浮点数计算可能会带来一个新的舍入错误

#引用模块解决除法
#对于需要非常精确的情况，可以使用 decimal 模块，它实现的十进制运算适合会计方面的应用和高精度要求的应用
#fractions 模块支持另外一种形式的运算，它实现的运算基于有理数（因此像1/3这样的数字可以精确地表示）
#最高要求则可是使用由 SciPy提供的 Numerical Python 包和其它用于数学和统计学的包

#形式1：import module-name。import后面跟空格，然后是模块名称，例如：import os
#形式2：from module1 import module11。module1是一个大模块，里面还有子模块module11，只想用module11，就这么写了
print()

#余数
#用%符号来取得两个数相除的余数
print("10除以3的余数是", 10%3)
print()

#使用内置函数divmod()
print("10除以3的(商，余数) ：", divmod(10,3))
print()

#四舍五入
#内建函数：round()
#浮点数中的十进制转化为二进制惹的祸
print("10除以3保留2位小数：", round(10/3,2))
print("1.235保留2位小数：", round(1.235,2))
print("1.2345保留3位小数：", round(1.2345,3))  #注意
print("2.235保留2位小数：", round(2.235,2))    #注意
print()

#常用数学函数和运算优先级
#python中的一个模块：Math
import math
#Pi =  3.141592653589793
print("Pi = ", math.pi)
print("math模块中包含函数：", dir(math))
#计算x的y次方
print("math模块中pow函数帮助文档：", help(math.pow))
print("math.pow(2,3)的值为：", math.pow(2,3))
print()
#常用数据函数
#绝对值abs
#四舍五入round

#运算优先级



#实践
#!python3
#coding:utf-8
#设置代码编码格式
print("hello world")



print()
#字符串
print("\'123\' 打印结果：",'123')
print("\"123\" 打印结果：","123")
print("123" + "456")
print("123" + str(456))
print("123" + repr(456))
print()

#转义字符
#\r  \t  \f   \x0a


#raw_input和print
#https://docs.python.org/2/library/functions.html  查看内建函数

#raw_input() 找不到？ python3使用input代替
help(input)
#x=input("Please input your name: ")
print()
#print("I have got your name " + str(x))
print()


#原始字符串
y=r"my worddir is '/Users/dai'"
print(y)
z='''my worddir is "/Users/dai"'''
print(z)
print()


#切片与索引
x1="name"
print(x1[0])
print(x1.index('e'))
print(x1[1:3])
print(x1[1:])

print()

#基本操作
print("abc" + "efg")
print("a in abc : ", "a" in "abc")
#cmp python3已失效
#print("compare aaa and bbb :" cmp("aaa","bbb"))
import operator
print("compare aaa > bbb :", operator.gt("aaa","bbb"))
print("compare aaa = bbb :", operator.eq("aaa","bbb"))
print("compare aaa < bbb :", operator.lt("aaa","bbb"))
print()

#max & min
print("max(abcd) = ", max("abcd"))
print("min(abcd) = ", min("abcd"))
print("max(abcd,efgh,ijkl) = ", max("abcd","efgh","ijkl"))

#* 重复个数
print("*" * 20)

#len取长度
print("abc的长度为：",len("abc"))

#字符串（4）
#格式化输出
print("my name is %s"  % "kuang" )
print("I'm %d years old." % 30)
print()

#string.format()
print("my hometown is {0} at {1} provice".format("HengShan","HuNan"))
print("my hometown is {p1} at {p2} provice".format(p1="HengShan",p2="HuNan"))
print("my hometown is %(p1)s at %(p2)s provice" %{"p1":"HengShan", "p2":"HuNan"})
print()

#常用字符串方法
#help(str)
print("%s" % str.__add__("my ", "name is kuang"))
print("name is alpha: ", "name".isalpha())
print("aa bb cc".split(" "))
print(" hello ".strip())
print("My Name Is Kuang".lower().upper().isupper())

print("www.baidu.com")
print("www.baidu.com".split("."))
c="www.baidu.com".split(".")
print(".".join(c))


#字符串4
#字符编码
#ASCII  American Standard Code for Information Interchange 美国信息交换标准代码
#Unicode转换格式 Unicode Transformation Format, UTF
#UTF-8（8-bit Unicode Transformation Format）是一种针对Unicode的可变长度字符编码
#encode & decode
#python2默认的编码是ascii，通过encode可以将对象的编码转换为指定编码格式（称作“编码”），而decode是这个过程的逆过程（称作“解码”）
a="中"
print(type(a))
print(a)
print(len(a))

#python2默认的是ASCII，python3默认的是utf-8

#提倡使用utf-8编码方案，因为它跨平台不错
#经验总结
#  1.以# coding:utf-8 开头
#  2.遇到字符（节）串，立刻转化为unicode，不要用str()，直接使用unicode()
#  3.如果对文件操作，打开文件的时候，最好用codecs.open，替代open(这个后面会讲到，先放在这里)
#  4.经验四：声明字符串直接加u，声明的字符串就是unicode编码的字符串
#byte——decode（解码）方法——》str——>encode（编码）方法——》byte
print()
us=u'中文'
print(type(us))
print(type(b'us'))
print(type(b'us'.decode('utf-8')))
print(type('us'.encode('utf-8')))
print("="*43)


#列表list-1
print("="*43)
a=[]
print(a,bool(a))
a=['123',4,"567890123"]
print(a,bool(a))
#切片与索引
print(a[0],a[1],a[2],  a[:2], a[1:], a[2][3:5])
print("="*43)

#索引
print(a.index(4))
#从右边开始编号，第-1号是右边第一个。但是，如果要切片的话，应该注意了
print(a[-1])

#反转
#列表反转
print(a[::-1])
#字符串反转
print(a[2][::-1])
#函数reversed
print(list(reversed(a)))
print(list(reversed("abcdefg")))
print("="*43)

#list 操作方法
print(a)
print("列表a的长度是：",len(a))
ap = ["good","python","I"]
print(ap)
aq = ["love","you"]
print(aq)
#连接+
print(ap+aq)
#重复*
print(ap * 2)
#存在in
print("good" in ap)
#max和min
print(max(ap))
print(min(ap))
#append
ap.append("append")
print(ap)
ap[len(ap):] = ['add']
print(ap)
#比较
print(operator.lt(ap,aq))
print("="*43)
print()

#列表list-2
print("="*43)
print()
#list函数 append和extend
#list.extend(L) ： Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.
ae=["1","2","3"]
print(ae)
ae[len(ae):] = ["4","5"]
print(ae)
ae[len(ae):] = "678"   #当作列表，将列表中每个元素逐个追加
print(ae)
#ae.extend("90")   #当作列表，将列表中每个元素逐个追加
ae.append("90")   #当作整体，追加到末尾
print(ae)
#append是整建制地追加，extend是个体化扩编
#都是原地修改列表
#既然是原地修改，就不返回值，就不能赋值给某个变量


print("="*43)
print()
#count函数
print(ae.count('5'))  #统计列表中含有指定元素的个数
print(len(ae))  #统计列表总共多少个元素

print("="*43)
print()
#index函数
#指定元素的位置下标
print(ae.index("90"))
#如果不存在，则报错
#list.index(x)：Return the index in the list of the first item whose value is x. It is an error if there is no such item.

print("="*43)
print()
#列表list-3
#insert
#list.insert(i, x): Insert an item at a given position.
# The first argument is the index of the element before which to insert,
# so a.insert(0, x) inserts at the front of the list,
# and a.insert(len(a), x) is equivalent to a.append(x).
ae.insert(3,"drm")
print(ae)
ae.insert(0,"frt")
print(ae)
ae.insert(len(ae),"end")
print(ae)
#如果遇到那个i已经超过了最大索引值，会自动将所要插入的元素放到列表的尾部，即追加
print("="*43)
print()

#pop和remove  删除list元素的方法
#list.pop([i])
#Remove the item at the given position in the list, and return it.
# If no index is specified, a.pop() removes and returns the last item in the list.
# (The square brackets around the i in the method signature denote that the parameter is optional,
# not that you should type square brackets at that position.
# You will see this notation frequently in the Python Library Reference.)
ap=["ab","cd","ef"]
print(ap)
ap.remove("ab")
print(ap)
#ap.remove("gh")
if "gh" in ap:
    print("got gh")
    ap.remove("gh")
else:
    print("failed")
print()

apop=["ab","cd","ef","gh","ij"]
print(apop.pop())
print(apop)
print(apop.pop(0))
print(apop)
#print(apop.pop(10))
print(apop)
i=10
if i < len(apop):
    print("got it")
    print(apop.pop(i))
else:
    print("failed")
print()

print("="*43)
print()

#reverse
#原地反过来，不是另外生成一个新的列表
apop.reverse()
print(apop)
#因为list.reverse()不返回值，所以不能实现对列表的反向迭代，如果要这么做，可以使用reversed函数

print("="*43)
print()
#sort
#L.sort(cmp=None, key=None, reverse=False) -- stable sort IN PLACE; cmp(x, y) -> -1, 0, 1
lst = ["python","java","c","pascal","basic"]
lst.sort()
print(lst)

#以字符串的长度为关键词进行排序
lst.sort(key=len)
print(lst)
print()

print("="*43)
print()

#list是可以改变的，str不可变

#多维list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0], " and ", matrix[1][0])
print()
print("="*43)
print()
#list和str转化
#str.split([sep] [,maxsplit])
#([sep]).join(list)
s = "I am, writing\npython\tbook on line"
print(s)
t=s.split()
print(t)
r=" ".join(t)
print(r)

print(r.split(","))
print("".join(r.split(",")))
print()

print("="*43)
print()

# tuple - 元组
#元组是用圆括号括起来的，其中的元素之间用逗号隔开。（都是英文半角）
#这种类型，可以歪着想，所谓“元”组，就是用“圆”括号啦
s = 1 , 3, "5" , ["a","b"]
print(s)

# tuple是一种序列类型的数据，这点上跟list/str类似。
# 它的特点就是其中的元素【不能更改】，这点上跟list不同，倒是跟str类似；
# 它的元素又可以是【任何类型】的数据，这点上跟list相同，但不同于str
print(type((3)))
print(type((3,)))

print("="*43)
print()

#索引和切片
t = (1, '23', [123, 'abc'], ('python', 'learn'))
print(t)
print(t[2][0])

print("="*43)
print()

#所有在list中可以修改list的方法，在tuple中，都失效
#用list()和tuple()能够实现两者的转化
tlst = list(t)
print(tlst)
ttpl = tuple(tlst)
print(ttpl)

print("="*43)
print()

#一般认为,tuple有这类特点,并且也是它使用的情景:
# 1.Tuple 比 list 操作速度快。如果您定义了一个值的常量集，并且唯一要用它做的是不断地遍历它，请使用 tuple 代替 list。
# 2.如果对不需要修改的数据进行 “写保护”，可以使代码更安全。使用 tuple 而不是 list 如同拥有一个隐含的 assert 语句，说明这一数据是常量。
#   如果必须要改变这些值，则需要执行 tuple 到 list 的转换 (需要使用一个特殊的函数)。
# 3.Tuples 可以在 dictionary（字典，后面要讲述） 中被用做 key，但是 list 不行。Dictionary key 必须是不可变的。
#   Tuple 本身是不可改变的，但是如果您有一个 list 的 tuple，那就认为是可变的了，用做 dictionary key 就是不安全的。
#   只有字符串、整数或其它对 dictionary 安全的 tuple 才可以用作 dictionary key。
# 4.Tuples 可以用在字符串格式化中。


#字典：先查索引（不管是拼音还是偏旁查字），然后通过索引找到相应内容。不用从头开始一页一页地找。
#正是基于这种需要，python中有了一种叫做dictionary的数据类型，翻译过来就是“字典”，用dict表示。

#1.创建一个空的dict，这个空dict，可以在以后向里面加东西用
mydict = {}
print(mydict)
print("="*43)
print()

#键值对 :前面的name叫做键（key），后面的qiwsir是前面的键所对应的值(value)
person = {"name":"qiwsir","site":"qiwsir.github.io","language":"python"}
print(person)
#键是唯一的，不能重复
print("language : ", person["language"])

print("="*43)
print()
#2.利用元组在建构字典
name = (["first","Google"],["second","Yahoo"])
website = dict(name)
print(website)

print("="*43)
print()

ad = dict(name = "qiwsir", age = 42)
print(ad)
print("="*43)
print()

#3.使用fromkeys,这种方法是重新建立一个dict
website = {}.fromkeys(("third","forth"),"facebook")
print(website)

print("="*43)
print()


#需要提醒注意的是，在字典中的“键”，必须是不可变的数据类型；“值”可以是任意数据类型。
dd = {(1,2):1}  #其中将键值设置为tuple 是不可重写的
print(dd)
#dd = {[1,2]:1}  其中将键值设置为list 是可重写的
print(dd)
print("="*43)
print()

#dict 因为它没有顺序，所以，在字典中就不要什么索引和切片了

#基本操作

#len(d)，返回字典(d)中的键值对的数量
#d[key]，返回字典(d)中的键(key)的值
#d[key]=value，将值(value)赋给字典(d)中的键(key)
#del d[key]，删除字典(d)的键(key)项（将该键值对删除）
#key in d，检查字典(d)中是否含有键为key的项

#字符串格式化输出

city_code = {"suzhou":"0512", "tangshan":"0315", "hangzhou":"0571"}
print(" Suzhou is a beautiful city, its area code is %(suzhou)s" % city_code)

print()
print("="*43)

temp = "<html><head><title>%(lang)s<title><body><p>My name is %(name)s.</p></body></head></html>"
my = {"name":"qiwsir", "lang":"python"}
print(temp % my)
print()
print("="*43)


#字典2
#copy

ad = {"name":"qiwsir", "lang":"python"}
bd = ad
print(ad," and ",bd)

print(id(ad), " and ", id(bd))
print()
print("="*43)


#这次得到的cd是跟原来的ad不同的，它在内存中另辟了一个空间。如果我尝试修改cd，就应该对原来的ad不会造成任何影响
cd = ad.copy()
print(cd, " and ", id(cd))

cd["name"] = "itdiffer.com"
print("copy :", cd, " and ", id(cd))

print()
print("="*43)

#对象有类型而变量无类型
print(bd, " and ", id(bd))
bd["name"] = "laoqi"
print(ad, " and ", id(ad))
print(bd, " and ", id(bd))

#copy 是在新开辟的一块内存空间，将原来的数据 复制过来。 新的内存任何改变与原对象无关
#=赋值的方法，是两个变量指向同一个对象，其中一个变量修改了对象的内容，等于两个变量都改变了内容

x = {"name":"qiwsir", "lang":["python", "java", "c"]}
y = x.copy()
print("Before : x = ", x, " 地址 :", id(x) )
print("Before : y = ", y, " 地址 :", id(y) )
y["lang"].remove("c")
print("After : x = ", x, " 地址 :", id(x) )
print("After : y = ", y, " 地址 :", id(y) )
#why??
print()
print("="*43)

#x["name"],y["name"]指向同一个内存地址 ==> 字符串"qiwsir"
#x["lang"],y["lang"]指向同一个内存地址 ==> 列表['python', 'java']
print("字符串：x[name]的地址：", id(x["name"]), "内容：", x["name"])
print("字符串：y[name]的地址：", id(y["name"]), "内容：", y["name"])
print("列  表：x[lang]的地址：", id(x["lang"]), "内容：", x["lang"])
print("列  表：y[lang]的地址：", id(y["lang"]), "内容：", y["lang"])
print()
print("="*43)

#将y["name"]指向新的 字符串地址"laoqi"
y["name"] = "laoqi"
print("字符串：x[name]的地址：", id(x["name"]), "内容：", x["name"])
print("字符串：y[name]的地址：", id(y["name"]), "内容：", y["name"])
print()
print("="*43)


y["lang"][0] = "php"
print("列  表：x[lang]的地址：", id(x["lang"]), "内容：", x["lang"])
print("列  表：y[lang]的地址：", id(y["lang"]), "内容：", y["lang"])
print()
print("="*43)

#x,y对应着两个不同对象，的确如此。但这个对象（字典）是由两个键值对组成的。其中一个键的值是列表。
#列表是同一个对象

########################################################################################################################
#
#  深层的原因，这跟python存储的数据类型特点有关，python只存储基本类型的数据，比如int,str，
#  对于不是基础类型的，比如刚才字典的值是列表，python不会在被复制的那个对象中重新存储，而是用引用的方式，指向原来的值
#
########################################################################################################################


#的确是，在python中，有一个“深拷贝”(deep copy)。不过，要用下一import来导入一个模块
import copy
z = copy.deepcopy(x)
print("new : x = ", x, " 地址 :", id(x) )
print("new : z = ", z, " 地址 :", id(z) )


print("字符串：x[name]的地址：", id(x["name"]), "内容：", x["name"])
print("字符串：z[name]的地址：", id(z["name"]), "内容：", z["name"])
print("列  表：x[lang]的地址：", id(x["lang"]), "内容：", x["lang"])
print("列  表：z[lang]的地址：", id(z["lang"]), "内容：", z["lang"])

print()
print("="*43)
x["lang"].remove("java")
x["lang"].append("c++")
print("列  表：x[lang]的地址：", id(x["lang"]), "内容：", x["lang"])
print("列  表：z[lang]的地址：", id(z["lang"]), "内容：", z["lang"])
print()
print("="*43)


#clear
#一个清空字典中所有元素的操作
a = {"name":"qiwsir"}
print(a)
a.clear()
print(a)
print()
print("="*43)

#get & setdefault
d={'lang':'Chinese'}
print(d.get('lang'))
#与用索引下标取值区别是：get方法获取不到key：value，则返回none
print(d.get('name'))

print("获取不到name则使用默认值：kuang：")
print(d.get('name','kuang'))

#获取不到，则新增该键值，如果存在则不新增
d.setdefault('hometown','Hunan')
print("d: ", d)
d.setdefault('hometown','Hengshan Hunan Province')
print("d: ", d)

d.setdefault('favorate')  #value is none
print("d: ", d)
print()
print("="*43)

#items/iteritems, keys/iterkeys, values/itervalues
# dict.item(): 得到一个关于字典的列表，列表中的元素是由字典中的键和值组成的元组
# D.items() -> list of D's (key, value) pairs, as 2-tuples
dd = {"name":"qiwsir", "lang":"python", "web":"www.itdiffer.com"}
dd_kv = dd.items()
print("关于字典的一个列表：", dd_kv)
print()
print("="*43)

# D.iteritems() -> an iterator over the (key, value) items of D
# 得到的是一个“迭代器”，这个迭代器是关于“D.items()”的
dd_iter = dd.__iter__()
print("dd_iter 类型是：",type(dd_iter), "dd_iter 打印结果是：", dd_iter)
#python3 无iteritems
# Python 3.x 里面，iteritems() 和 viewitems() 这两个方法都已经废除了，
# 而 items() 得到的结果是和 2.x 里面 viewitems() 一致的。
# 在3.x 里 用 items()替换iteritems() ，可以用于 for 来循环遍历
print()
print("="*43)

class Person(object):

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k, v in kw.items():
            setattr(self, k, v)

p = Person('Bob', 'Male', age=18, course='Python')

print(p.name)
print(p.gender)
print(p.age)
print(p.course)

print()
print("="*43)

#keys, values
print("dd的值为：",dd)
dd_key=dd.keys()
print("dd_key 的值为：", dd_key, "类型：", type(dd_key))
dd_val=dd.values()
print("dd_val 的值为：", dd_val, "类型：", type(dd_val))


print()
print("="*43)

#pop, popitem
#D.pop(k[,d])是以字典的键为参数，删除指定键的键值对。
print("dd的值为：",dd)
#删除指定键"name"，返回了其值"qiwsir"。这样，在原字典中，“'name':'qiwsir'”这个键值对就被删除了
dd.pop("name")
print("dd的值为：",dd)
#值得注意的是，pop函数中的参数是不能省略的，这跟列表中的那个pop有所不同
dx=dd.pop("xxx","x-value")  #不存在xxx的键，则默认返回x-value,原dd不变，如果不设置第二个参数，不存在则直接报错
print("dx的值为：",dx)
print()
print("="*43)
#D.popitem()， 与list.pop()有相似之处，不用写参数（list.pop是可以不写参数）
#随机删除一个，并将所删除的返回，如果字典是空的，就要报错了
print("dd 被随机删除一个后：",dd.popitem())
print()
print("="*43)

#update
#字典d2更新入了d1那个字典，于是d1中就多了一些内容，把d2的内容包含进来了。d2当然还存在，并没有受到影响
d1 = {"lang":"python"}
d2 = {"song":"I dreamed a dream"}
print("d1: ",d1, " & d2: ",d2)
d1.update(d2)
print("update d1: ",d1, " & d2: ",d2)
#或者
d2.update([("name","qiwsir"), ("web","itdiffer.com")])
print("update d1: ",d1, " & d2: ",d2)

print()
print("="*43)

#has_key
#print(d2.has_key("web"))
#python3 无该用法， 改成使用 in
print("d2 : ", d2)
if "web" in d2 :
    print("has")
else:
    print("no")

print()
print("="*43)

print()
print("===========================================")
print("Done!!!")
print("===========================================")
