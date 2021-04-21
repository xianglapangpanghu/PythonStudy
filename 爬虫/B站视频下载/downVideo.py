import requests
import os
import tqdm

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Host': 'api.bilibili.com',
    'Origin': 'https://www.bilibili.com',
    'Cookie': '_uuid=B08961E7-5248-E19E-292D-CF9DABFF980E92321infoc; buvid3=4B8BFA74-705D-4E3B-AFDE-EE513DEFB7AE143100infoc; sid=6epr8zei; DedeUserID=385385418; DedeUserID__ckMd5=d8bd01c12e87aec2; SESSDATA=441b4874%2C1619517584%2C5c71f*a1; bili_jct=fbd22c3bc81b1b1761df679f8dd77954; LIVE_BUVID=AUTO9016039656786639; PVID=1; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(J|)RRlmJ)|0JuY|R)Rullk; bp_t_offset_385385418=458631116269323134; bp_video_offset_385385418=463816176887860111; CURRENT_QUALITY=112; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f'
}
def downUrl(url):
    r = requests.get(url,headers = headers)
    durl = r.json()['data']['durl'][0]['url']
    print(durl)
    

def main():
    url = 'https://api.bilibili.com/x/player/playurl?cid=214629055&bvid=BV1fz4y1D7tU&qn=80'
    downUrl(url)

if __name__ == "__main__":
    main()