import requests
from lxml import etree
import time

def getHTML(url):#获取网页
    try:
        headers = {
            'Cookie': 'track_id=139715681590804480; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22pcbiaoti%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22track_id%22%3A%22139715681590804480%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22e57db0dd-9ae3-48e0-80b5-aded8bc53590%22%2C%22ca_city%22%3A%22nc%22%2C%22sessionid%22%3A%22ddfb27f9-606f-4fe4-d60c-2c95d8629a86%22%7D; uuid=e57db0dd-9ae3-48e0-80b5-aded8bc53590; antipas=691Iry6148l8GSg02m855c65; cityDomain=dl; user_city_id=214; preTime=%7B%22last%22%3A1604495870%2C%22this%22%3A1604466014%2C%22pre%22%3A1604466014%7D; ganji_uuid=7698028013342973489368; lg=1; Hm_lvt_bf3ee5b290ce731c7a4ce7a617256354=1604495872,1604556544; sessionid=04091cea-626a-4292-c0dc-8807575f9085; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A50943698757%7D; Hm_lpvt_bf3ee5b290ce731c7a4ce7a617256354=1604556544',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'
        }
        s = requests.session()
        r = s.get(url, headers = headers)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        time.sleep(1)
        return r.content
    except:
        return "error"

def get_carURL(text):#解析获得每辆汽车详情页面url
    try:
        html = etree.HTML(text)
        #print(etree.tostring(html))
        ul = html.xpath('//ul[@class="carlist clearfix js-top"]')[0]
        lis = ul.xpath('./li')
        carURLs = []
        for li in lis:
             carURL = 'https://www.guazi.com' + li.xpath('./a/@href')[0]
             carURLs.append(carURL)
        return carURLs
    except:
        return "error:get_carURL"

def infoCar(carURL):#获取每辆汽车详细信息
    try:
        html = getHTML(carURL)
        html = etree.HTML(html)
        # print(carURL)
        title = html.xpath('normalize-space(//div[@class="product-textbox"]//h1/text())')
        info = html.xpath('//div[@class="product-textbox"]/ul/li/span/text()')
        #print(title)
        infos = {}
        Km = info[2]
        Displacement = info[3]
        Gearbox = info[4]
        infos['车名'] = title
        infos['表显里程'] = Km
        infos['排量'] = Displacement
        infos['变速箱'] = Gearbox
        print(infos)
        return ""
    except:
        return "error:infoCar"
def main():
    url = 'https://www.guazi.com/nc/buy/o2/'
    html = getHTML(url)
    carURLs = get_carURL(html)
    # infoCar(carURLs[0])
    for carURL in carURLs:
        infoCar(carURL)

if __name__ == "__main__":
    main()