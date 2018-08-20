#Function函数
#定义函数的格式为：
#def 函数名(参数1，参数2，...，参数n)：
#    函数体（语句块）

#变量无类型，只有对象才有类型
#python不用在定义函数的时候告诉函数参数的数据类型 ！！！！
#这里的所谓参数，跟前面说的变量，本质上是一回事。只有当用到该变量的时候，才建立变量与对象的对应关系，否则，关系不建立。
# 而对象才有类型。那么，在add(x,y)函数中，x,y在引用对象之前，是完全飘忽的，没有被贴在任何一个对象上，换句话说它们有可能引用任何对象，
# 只要后面的运算许可，如果后面的运算不许可，则会报错

#result = add(x,y)在被运行之前，计算机内是不存在的，直到代码运行到这里的时候，在计算机中，就建立起来了一个对象，
# 这就如同前面所学习过的字符串、列表等类型的对象一样，运行add(x,y)之后，也建立了一个add(x,y)的对象，这个对象与变量result可以建立引用关系，
# 并且add(x,y)将运算结果返回

#函数返回多个值，即返回元组  return x, y, z


def my_fun():
    """
    this is my test function
    :return: none
    """
    print("this is my_fun!")

my_fun()
print(my_fun.__doc__)


global x  #全局变量


#不确定参数个数 *arg 名称可以不一样，但是符号必须要有） 不确定部分当作一个整体：元组. 可遍历：  for i  in arg

#除了用args这种形式的参数接收多个值之外，还可以用*kargs的形式接收数值，不过这次有点不一样
#如果用**kargs的形式收集值，会得到dict类型的数据，但是，需要在传值的时候说明“键”和“值”，因为在字典中是以键值对形式出现的
def foo(x,y,z,*args,**kargs):
    print(x)
    print(y)
    print(z)
    print(args)
    print(kargs)

foo(1,2,3,4,5,name="qiwsir")

#使用一个星号*，是以元组形式传值，如果用**的方式，以字典的形式




# 表达式
#lambda做为一个单行的函数，在编程实践中，可以选择使用。

#总结一下lambda函数的使用方法：
#在lambda后面直接跟变量
#变量后面是冒号
#冒号后面是表达式，表达式计算结果就是本函数的返回值

#map
#map()是python的一个内置函数，它的基本样式是： map(func,seq)

#func是一个函数，seq是一个序列对象。
# 在执行的时候，序列对象中的每个元素，按照从左到右的顺序，依次被取出来，并塞入到func那个函数里面，并将func的返回值依次存到一个list中
items = [1,2,3,4,5]
squared = []
for i in items:
    squared.append(i**2)
print(squared)


def sqr(x): return x**2

map(sqr,items)  #返回一个map对象

map(lambda x: x**2, items)


e3=[ x**2 for x in items ]
print(e3)    #这个我最喜欢了，一般情况下速度足够快，而且可读性强




#Unit 1
#解一元二次方程
#解一元二次方程，是初中数学中的基本知识，一般来讲解法有：公式法、因式分解法等。读者可以根据自己的理解，写一段求解一元二次方程的程序。
# 一元二次方程形式:a * x^2 + b * x + c = 0 (a≠0，且a，b，c是常数)。
# x1 = (-b + sqr(b^2 -4ac))/2a
# x2 = (-b - sqr(b^2 -4ac))/2a
import math

# x^2 + x - 12 = 0
print("\n解一元二次方程：ax^2 + bx + c = 0 \n")
def func_rslt_v0(x,y,z):

    delta = pow(y,2) - (4 * x * z)   #delta 不能小于0

    if delta < 0:
        return False

    elif delta == 0:
        retun (-1 * y )/(2*x)

    else:
        r1 = (-1 * y + math.sqrt(delta) )/ (2 * x)
        r2 = (-1 * y - math.sqrt(delta) ) / (2 * x)
        return r1,r2

num=(1,1,-12)
print("a,b,c 参数：",num, "\n")
t = func_rslt_v0(*num)

print("解 = ", t)

#改进：
#如果不小心将第一个系数(a)的值输入了0，程序肯定会报错。如何避免之？要记住，任何人的输入都是不可靠的
#结果貌似只能是小数，这在某些情况下是近似值，能不能得到以分数形式表示的精确结果呢？
#复数，python是可以表示复数的，如果delta<0，是不是写成复数更好，毕竟我是学过高中数学的。


#统计考试成绩
#每次考试之后，教师都要统计考试成绩，一般包括：平均分，对所有人按成绩从高到低排队，谁成绩最好，谁成绩最差。
c1={"zhangsan":90, "lisi":78, "wangermazi":39}
#最高分或者最低分，可能有人并列
#要实现不同长度的字典作为输入值
#输出结果中，除了平均分，其它的都要有姓名和分数两项

def average_score(scores):
    """
    统计平均分.
    """
    score_values = scores.values()
    sum_scores = sum(score_values)
    average = sum_scores/len(score_values)
    return average

def sorted_score(scores):
    """
    对成绩从高到低排队.
    """
    score_lst = [(scores[k],k) for k in scores]
    sort_lst = sorted(score_lst, reverse=True)   #以元组为元素的列表 排序
    return [(i[1], i[0]) for i in sort_lst]
    #[('zhangsan', 90), ('lisi', 78), ('wangermazi', 39)], 其中for迭代第一个成员时i[1]代表'90'，i[0]代表'zhangsan'

def max_score(scores):
    """
    成绩最高的姓名和分数.
    """
    lst = sorted_score(scores)    #引用分数排序的函数sorted_score
    max_score = lst[0][1]
    return [(i[0],i[1]) for i in lst if i[1]==max_score]  #如果分数与最高分相等则返回所有匹配的姓名和分数

def min_score(scores):
    """
    成绩最低的姓名和分数.
    """
    lst = sorted_score(scores)
    min_score = lst[len(lst)-1][1]
    return [(i[0],i[1]) for i in lst if i[1]==min_score]  #如果分数与最低分相等则返回所有匹配的姓名和分数

if __name__ == "__main__":
    examine_scores = {"google":98, "facebook":99, "baidu":52, "alibaba":80, "yahoo":49, "IBM":70, "android":76, "apple":99, "amazon":99}

    ave = average_score(examine_scores)
    print("the average score is: ",ave )   #平均分

    sor = sorted_score(examine_scores)
    print("list of the scores: ",sor)      #成绩表

    xueba = max_score(examine_scores)
    print("Xueba is: ",xueba)              #学霸们

    xuezha = min_score(examine_scores)
    print("Xuzha is: ",xuezha)             #学渣们


###
#    强调[(i[0],i[1]) for i in lst if i[1]==min_score]用法
###



#找素数
#找出100以内的素数
#質數（Prime number），又称素数，指在大於1的自然数中，除了1和此整数自身外，無法被其他自然数整除的数（也可定義為只有1和本身两个因数的数）

import math

def is_prime(n):
    """
    判断一个数是否是素数
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    primes = [i for i in range(2,100) if is_prime(i)]    #从2开始，因为1显然不是质数
    print(primes)

#编写函数，在开发实践中是非常必要和常见的，一般情况，你写的函数应该是：

#尽量不要使用全局变量。
#如果参数是可变类型数据，在函数内，不要修改它。
#每个函数的功能和目标要单纯，不要试图一个函数做很多事情。
#函数的代码行数尽量少。
#函数的独立性越强越好，不要跟其它的外部东西产生关联。

