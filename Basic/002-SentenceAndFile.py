#Unit 1
# 有一个列表，其中包括10个元素，例如这个列表是[1,2,3,4,5,6,7,8,9,0],要求将列表中的每个元素一次向前移动一个位置，
# 第一个元素到列表的最后，然后输出这个列表。
# 最终样式是[2,3,4,5,6,7,8,9,0,1]

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

