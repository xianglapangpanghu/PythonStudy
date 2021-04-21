import requests
import threading
import queue
from urllib import parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Referer': 'https://pvp.qq.com/web201605/wallpaper.shtml'
}

class Producer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        threading.Thread.__init__(self)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while not self.page_queue.empty():
            page_url = self.page_queue.get()
            r = requests.get(page_url, headers = headers)
            data = r.json()['List']
            for i in data:
                print(i)

class Consumer(threading.Thread):
    def __init__(self, img_queue, *args, **kwargs):
        threading.Thread.__init__(self)
        pass

def main():
    page_queue = queue.Queue(23)
    img_queue = queue.Queue(888)

    for i in range(1):
        page_url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1606989962871'.format(i)
        page_queue.put(page_url)
        
    for i in range(1):
        th = Producer(page_queue, img_queue, name = "消费者线程%d号"%i)
        th.start()

    for i in range(1):
        th = Consumer(page_queue, img_queue, name = "生产者线程%d号"%i)
        # th.start()
    

if __name__ == "__main__":
    main()