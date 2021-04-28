# scrapy学习笔记

>[官网](https://scrapy.org/)

>[官方文档](https://docs.scrapy.org/en/latest/)

---

# [scrapy框架图](https://pic1.zhimg.com/v2-8c591d54457bb033812a2b0364011e9c_1440w.jpg?source=172ae18b,"框架图")

5+2模型:5个基础模块+2扩展模块
scrapy engine(引擎):scrapy的核心,负责各模块之间的调度和通信.

spider(爬虫):把需要的链接请求发送给scrapy engine引擎,最后引擎把请求返回的数据发送给爬虫解析.

schedule(调度器):处理引擎的请求,排列,调整,请求顺序等.

downloader(下载器):专门处理下载请求的模块,下载数据并返回给引擎.

item pipeline(管道):负责数据的存储.

downloader Middleware(下载器中间件):下载器和引擎之间的通讯.

spider Middleware(爬虫中间件):爬虫和引擎之间通信的中间件.

创建项目：scrapy startproject [项目名称]
进入项目： cd [项目名称]
创建爬虫：scrapy genspider [爬虫名称][爬虫作用域]
爬虫名称不能跟项目名称一样

----

创建crawl爬虫
创建项目：scrapy startproject [项目名称]
进入项目： cd [项目名称]
创建crawl爬虫项目：scrapy genspider -t crawl [爬虫名称][爬虫作用域]

---

创建完成后，首先配置setting，关闭robot协议验证，更换请求头，开启管道（文件存储用到），配置数据库
>配置数据库代码
MYSQL_CONFIGP = {
  'DRIVER': "数据库驱动程序",
  'HOST': "数据库的地址",
  'PORT': 数据库端口,
  'USER': "用户名",
  'PASSWORD': "密码",
  'DATABASE': "数据库名"
}

>LOG_LEVEL = "WARNING"输出warning等级以上

>LOG.FILE = "./log.log"日志输出位置

---

测试网页解析可以用：scrapy shell [url]进入，调用各类方法来测试

解析网页的返回item最好用yield函数

---

># 图片的下载
>

>## 1.首先在item下添加两个字段，image_urls，images（名字不能改）

>## 2.开启pipline，配置setting

ITEM_PIPELINES = {
   #'DownLoad_ZCOOL.pipelines.DownloadZcoolPipeline': 300,
   'scrapy.pipelines.images.ImagesPipeline': 200, #使用这个来自动下载图片，后面数字是优先级，数字越小优先级越高
}
配置IMAGES_STORE = os.path.join(os.getcwd(),'images') #配置图片下载路径

>## 3.默认所有图片文件都保存在保存路径的full文件夹下，如果有需求，要重写ImagesPipeline中的file_path方法

ITEM_PIPELINES = {
   #'DownLoad_ZCOOL.pipelines.DownloadZcoolPipeline': 300, #可以使用默认的pipline，也可以自己定义
   #'scrapy.pipelines.images.ImagesPipeline': 200, #关掉之前开启的pipline
}

>在pipline.py中

```
import os #导入os模块
import re #导入正则模块，后面处理文件标题会用到
from itemadapter import ItemAdapter #创建默认加载，不用管
from scrapy.pipelines.images import ImagesPipeline #重写首先要导入相应模块
from DownLoad_ZCOOL import settings #导入setting配置文件

                #首先要继承ImagesPipeline这个模块
class DownloadZcoolPipeline(ImagesPipeline):
    #由于file_path模块没有item选项，所以要绑定一下，传过去
    def get_media_requests(self,item,info):
        media_requests =  super(DownloadZcoolPipeline, self).get_media_requests(item,info)
        for media_request in media_requests:
            media_request.item = item
        return media_requests

    def file_path(self, request, response=None, info=None):
        #默认的保存路径
        origin_path =  super(DownloadZcoolPipeline, self).file_path(request,response,info)
        #图片的标题
        title = request.item.get("title")
        #处理标题中不合法的字符串（不合法的字符无法创建文件夹）
        title = re.sub(r'[\\/:\*\?"<>\|]',"",title)
        #将总图片存储路径XXX/images和图片的标题拼接成xxx/images/title
        title_path = os.path.join(settings.IMAGES_STORE, title)
        #判断标题文件夹是否存在，不存在就创建
        if not os.path.exists(title_path):
            os.mkdir(title_path)
        #full/图片名 -> 图片名
        image_name = origin_path.replace("full/", "")
        #拼接图片路径
        image_path = os.path.join(title_path,image_name)
        return image_path
```
