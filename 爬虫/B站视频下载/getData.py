'''
通过BV/AV号获取每集视频的数据
'''
'''
https://api.bilibili.com/x/player/pagelist?bvid=BV1fz4y1D7tU&jsonp=jsonp
'''
import requests
import os
import csv

'''
获取数据
'''
def getData(url, bvid, path):
    # print(data)
    SavePath = path + '\Data_{}.csv'.format(bvid)
    print(SavePath)
    if not os.path.basename(SavePath):
        r = requests.get(url)
        data = r.json()['data']
        headers = ('cid','page','from','vupload','part','duration','vid','weblink','dimension')
        with open(SavePath,'w',encoding='utf-8') as fp:
            writer = csv.DictWriter(fp,headers)
            writer.writeheader()
            writer.writerows(data)
    else:
        print('文件{}已存在'.format(bvid))
    

def main():
    bvid = 'BV1fz4y1D7tU'
    url = 'https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp'.format(bvid)
    path = r"D:\python\PythonStudy\爬虫\B站视频下载\data" #数据保存目录
    getData(url,bvid,path)

if __name__ == "__main__":
    main()