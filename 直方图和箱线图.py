import numpy as np 
from matplotlib import pyplot as plt

data = np.load(r'F:\代码\np\国民经济核算季度数据.npz',allow_pickle=True)
plt.rcParams['font.sans-serif']='SimHei'#设置中文显示
name = data['columns']
values = data['values']

#直方图和饼图
p = plt.figure(figsize=(14,14))#设置画布

#子图1
a1=p.add_subplot(2,2,1)
value1 = values[67,6:15]
lable1 = ['农林', '工业', '建筑', '批发', '交通', '餐饮', '金融业', '房地产', '其他']
plt.xticks(range(9),lable1)
plt.title('2016年第四季度各产业国民生产总值直方图')

#设置
plt.xlabel('产业')
plt.ylabel('生产总值（亿元）')
plt.bar(range(9),value1,width=0.5)

#子图2
a2=p.add_subplot(2,2,2)
value2 = values[68,6:15]
lable2 = ['农林', '工业', '建筑', '批发', '交通', '餐饮', '金融业', '房地产', '其他']
plt.xticks(range(9),lable2)
plt.title('2017年第一季度各产业国民生产总值直方图')

#设置
plt.xlabel('产业')
plt.ylabel('生产总值（亿元）')
plt.bar(range(9),value2,width=0.5)

#子图3
a3 = p.add_subplot(2,2,3)
value3 = values[67,6:15]
lable3 = ['农林', '工业', '建筑', '批发', '交通', '餐饮', '金融业', '房地产', '其他']
plt.title('2016年第四季度各产业国民生产总值饼图')
plt.pie(value3,
        explode=(0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,),
        labels=lable3,
        autopct='%.1f%%')

#子图4
a3 = p.add_subplot(2,2,4)
value4 = values[68,6:15]
lable4 = ['农林', '工业', '建筑', '批发', '交通', '餐饮', '金融业', '房地产', '其他']
plt.title('2017年第一季度各产业国民生产总值饼图')
plt.pie(value4,
        explode=(0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,),
        labels=lable4,
        autopct='%.1f%%')

#箱线图
p2 = plt.figure(figsize=(10,10))
value5 = values[5:68,6:15]
lable5 = ['农林', '工业', '建筑', '批发', '交通', '餐饮', '金融业', '房地产', '其他']
plt.xlabel('产业')
plt.ylabel('生产总值（亿元）')
plt.title('2001-2017年各行业国民生产总值箱线图')
plt.boxplot(value5, notch= True, labels=lable5, meanline=True)
plt.show()