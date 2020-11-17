import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLTEXT(url):#获取网页
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "

def fillUnivList(ulist, html):#解析网页1
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds [1].string, tds[2].string, tds[3].string])

def printUnivList(ulist, num):#输出内容
    tplt = "{0:^10}\t{1:{4}^6}\t{2:^20}\t{2:^10}"
    print(tplt.format("排名","学校名称","省份","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3],chr(12288)))
    print("Suc" + str(num))

if __name__ == "__main__":
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html = getHTMLTEXT(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 10)
