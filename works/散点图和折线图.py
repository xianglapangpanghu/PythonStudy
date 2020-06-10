import numpy as np 
from matplotlib import pyplot as plt
data = np.load(r'F:\代码\np\populations.npz',allow_pickle=True)
plt.rcParams['font.sans-serif']='SimHei'#设置中文显示
plt.rcParams['axes.unicode_minus'] = False
value = data['data']
value = value[0:-2,:]
value = value[np.lexsort(value[:,::-1].T)]
name = data['feature_names']
#np.set_printoptions(threshold=np.NaN)

#创建画布
p = plt.figure(figsize=(12,12))
#散点图
a1 = p.add_subplot(1,2,1)
plt.xlabel('时间（年）')
plt.ylabel('人口')
plt.scatter(value[:,0],value[:,1], marker='o')
plt.scatter(value[:,0],value[:,2], marker='o')
plt.scatter(value[:,0],value[:,3], marker='o')
plt.scatter(value[:,0],value[:,4], marker='o')
plt.scatter(value[:,0],value[:,5], marker='o')
plt.xticks(rotation = 30)
plt.legend(['年末总人口','男性人口','女性人口','城镇人口','乡村人口'])
plt.title('1996-2015年各个特征随着年份推移发生的变化情况散点图')
plt.savefig('1996-2015年各个特征随着年份推移发生的变化情况散点图.png')

#折线图
a1 = p.add_subplot(1,2,2)
plt.xlabel('时间（年）')
plt.ylabel('人口')
plt.plot(value[:,0],value[:,1], marker='o')
plt.plot(value[:,0],value[:,2], marker='o')
plt.plot(value[:,0],value[:,3], marker='o')
plt.plot(value[:,0],value[:,4], marker='o')
plt.plot(value[:,0],value[:,5], marker='o')
plt.xticks(rotation = 30)
plt.legend(['年末总人口','男性人口','女性人口','城镇人口','乡村人口'])
plt.title('1996-2015年各个特征随着年份推移发生的变化情况散点图')
plt.savefig('1996-2015年各个特征随着年份推移发生的变化情况折线图.png')
plt.show()