# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import re
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from DownLoad_ZCOOL import settings

class DownloadZcoolPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        media_requests =  super(DownloadZcoolPipeline, self).get_media_requests(item,info)
        for media_request in media_requests:
            media_request.item = item
        return media_requests

    def file_path(self, request, response=None, info=None):
        origin_path =  super(DownloadZcoolPipeline, self).file_path(request,response,info)
        title = request.item.get("title")
        #处理标题中不合法的字符串
        title = re.sub(r'[\\/:\*\?"<>\|]',"",title)
        title_path = os.path.join(settings.IMAGES_STORE, title)
        if not os.path.exists(title_path):
            os.mkdir(title_path)
        image_name = origin_path.replace("full/", "")
        image_path = os.path.join(title_path,image_name)
        return image_path