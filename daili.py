from selenium import webdriver
import requests
import time

url="http://httpbin.org/ip"
ip="120.221.86.164"
port = "80"

proxy={"http":"http://"+ip+":"+port}
headers={"User-Agent":"Mozilla/5.0"}
res=requests.get(url,proxies=proxy,headers=headers)
print(res.text)  # 返回200：表示该ip代理是可用的
print('------------------')


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=120.221.86.164:80')
# 设置ip还有端口  
driver = webdriver.Chrome(options=chromeOptions)
driver.get(url)
time.sleep(10)
driver.quit()