#Unit 1
# 有一个列表，其中包括10个元素，例如这个列表是[1,2,3,4,5,6,7,8,9,0],要求将列表中的每个元素一次向前移动一个位置，
# 第一个元素到列表的最后，然后输出这个列表。
# 最终样式是[2,3,4,5,6,7,8,9,0,1]
print("Unit 1:")
list=[1,2,3,4,5,6,7,8,9,0]
new_list=[]

print("ori list => ", list)
for p in range(1,len(list)):
    new_list.append(list[p])
new_list.append(list[0])

print("new list => ", new_list)

#案例1
raw = [1,2,3,4,5,6,7,8,9,0]
print(raw)

b = raw.pop(0)
raw.append(b)
print(raw)


#Unit 2
# 产生一个列表，其中有40个元素，每个元素是0到100的一个随机整数
# 如果这个列表中的数据代表着某个班级40人的分数，请计算成绩低于平均分的学生人数，并输出
# 对上面的列表元素从大到小排序
print()
print("Unit 2:")
import random

point=[]
tot=0
for i in range(10):
    rd = random.randint(0, 100)
    tot+=rd
    point.append(rd)

avg=tot/len(point)
print("全体成绩：", point, " 平均分: %s" %(avg))

print("低于平均分的有：", end=' ')
low=0
for x in point:
    if x < avg :
        low+=1;
        print(x , end=' ')
print("总人数：%d" %(low), "个")
print("排序结果（降序）：", sorted(point,reverse=True))


#案例2

print("案例：")

score = [random.randint(0,100) for i in range(10)]    #0到100之间，随机得到40个整数，组成列表
print(score)

num = len(score)
sum_score = sum(score)               #对列表中的整数求和
ave_num = sum_score/num              #计算平均数
less_ave = len([i for i in score if i<ave_num])    #将小于平均数的找出来，组成新的列表，并度量该列表的长度
print("the average score is:%.1f" % ave_num)
print("There are %d students less than average." % less_ave)

sorted_score = sorted(score, reverse=True)    #对原列表排序
print(sorted_score)


print()
print("Unit 3:")
#Unit 3
#如果将一句话作为一个字符串，那么这个字符串中必然会有空格（这里仅讨论英文），比如"How are you."，
# 但有的时候，会在两个单词之间多大一个空格。现在的任务是，如果一个字符串中有连续的两个空格，请把它删除。
eg=open('/Users/dai/PycharmProjects/Basic/002/example.txt', 'w')
eg.write("Hello     Python 3.7\n")
eg.write("I'm practise it.\n")
eg.write("let's just  do it\n")
eg.close()

eg = open('/Users/dai/PycharmProjects/Basic/002/example.txt','r')
print("旧文件：")
for f in eg:
    print(f)

eg.seek(0)

print("新文件：")
for f in eg:
    #print(f.replace('  ', ' '))  #多个连续空格 只会去除一次双空格
    f1=f.split(" ")
    #print(f1)
    word=[s for s in f1 if s != ""]  #利用列表解析，将空格检出
    print(" ".join(word))
eg.close()

#Unit 4
#根據高德納（Donald Ervin Knuth）的《計算機程序設計藝術》（The Art of Computer Programming），
# 1150年印度數學家Gopala和金月在研究箱子包裝物件長宽剛好為1和2的可行方法數目時，首先描述這個數列。
# 在西方，最先研究這個數列的人是比薩的李奧納多（義大利人斐波那契 Leonardo Fibonacci），他描述兔子生長的數目時用上了這數列。
#第一個月初有一對剛誕生的兔子;第二個月之後（第三個月初）牠們可以生育,每月每對可生育的兔子會誕生下一對新兔子;兔子永不死去
#假設在n月有可生育的兔子總共a對，n+1月就總共有b對。在n+2月必定總共有a+b對： >因為在n+2月的時候，
# 前一月（n+1月）的b對兔子可以存留至第n+2月（在當月屬於新誕生的兔子尚不能生育）。而新生育出的兔子對數等於所有在n月就已存在的a對

#上面故事是一个著名的数列——斐波那契数列——的起源。斐波那契数列用数学方式表示就是：
#a0 = 0                (n=0)
#a1 = 1                (n=1)
#a[n] = a[n-1] + a[n-2]  (n>=2)
#我们要做的事情是用程序计算出n=100是的值。
print()
print("Unit 4: 斐波那契数列 ")
l1=[]
for p in range(0,100):
    if p == 0 :
        l1.append(0)
    if p == 1:
        l1.append(1)
    if p >= 2 :
        l1.append(l1[p-2] + l1[p-1])

print("斐波那契数列-100: ", l1[99])



print("\n案例：")
a, b = 0, 1

for i in range(99):    #改变这里的数，就能得到相应项的结果
    a, b = b, a+b

print(a)
