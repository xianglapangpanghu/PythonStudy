import re
import requests

def getHTMLText(url):
    try:
        headers = {
        'authority': 's.taobao.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '_samesite_flag_=true; cookie2=1d9efcdd67803569956401a000b64e8d; t=82df43e9470f6680caaaf8b8684f0ced; _tb_token_=fa53ba1eeef8b; cna=GrVKF89zM28CAXcADrjz8qWz; sgcookie=ESMm%2Bu4TWz8vzd7%2FfmxT0; unb=3434558979; uc3=lg2=V32FPkk%2Fw0dUvg%3D%3D&vt3=F8dBxGZuEXfb6MuTyeU%3D&id2=UNQ0ULl5MwAJyg%3D%3D&nk2=CNjsgRG0zQg%3D; csg=f614a961; lgc=ko2012re; cookie17=UNQ0ULl5MwAJyg%3D%3D; dnk=ko2012re; skt=71b6cc7d4ecd8385; existShop=MTU4OTg4ODgxOQ%3D%3D; uc4=nk4=0%40Cr0SrKHYZ6jwK3dTAi2z9tU5rA%3D%3D&id4=0%40UgP%2FqqnbLWsufLAkxuu8amiMxyMq; tracknick=ko2012re; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; sg=e9b; _nk_=ko2012re; cookie1=W8q9DLjLv5rrapjNZzH7exSo8al7KHtrqPyY9o9%2FHBU%3D; enc=rDDKCaAPRB4ruhKXLGGLHMmIMOARkdT2p%2FTvTcJMMN3z4QHTqNwsJtrveQtJfBhFPy88t6QVQ%2B47kUl5JS0j4A%3D%3D; tfstk=cWLcBbNe6nSjpvKXOS_XsTlrL5GRajaNKF8WzE13KjR6448PgsbU4ku8BbXDnFE1.; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=9_1; thw=cn; JSESSIONID=470EC3315B3C8F44D6AE237184CFB089; v=0; l=eBLtbwFlQZDNd4e2BO5Zourza77tZQOb4sPzaNbMiInca6B51FanrNQDibhvRdtjgt1FLetzEdARfRLHR3Ai02G3a3h2q_5rnxf..; isg=BJGRyC2Wq2PYr8d3JM3iKQPRoJ0r_gVwhf4aAnMlyNh3GrFsu07kQD9wvO78Ep2o; uc1=cookie14=UoTUM2ji1mTKPg%3D%3D&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&existShop=false&cookie21=WqG3DMC9Fbxq&cookie15=W5iHLLyFOGW7aA%3D%3D&pas=0',
        }
        r = requests.get(url, headers = headers)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'
    
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\":\"[\d.]*\"', html)
        tlt = re.findall(r'"raw_title":".*?"', html)
        #print(plt)
        #print(tlt)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("解析出错")
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
if __name__ == "__main__":
    goods = "书包"
    depth = 3
    start_url = "https://s.taobao.com/search?q=" + goods
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infolist, html)
        except:
            print(i)
            continue
    printGoodsList(infolist)