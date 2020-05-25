import os
import requests
from tqdm import tqdm
infolist = [['href="/rhdm/9014/"', 'target="_blank"', 'title="ロマンスは剣の輝きII"'], ['href="/rhdm/3520/"', 'target="_blank"', 'title="螢子"'], ['href="/rhdm/3482/"', 'target="_blank"', 'title="英才狂育"']]
downID = [['3130123826243292'], ['7132223843707405'], ['3130123826244877'], ['3130123826245388'], ['2150023851569055'], ['7154723843814748'], ['8130123162315690'], ['2150023179359085'], ['4151223158892094'], ['4132223158882432']]     
downPage = [6, 3, 1]
count = 0
src="https://271dm.applinzi.com/v.php?id="
for i in range(len(infolist)):
    root = "E://DownVedio//{}//".format(infolist[i][2][7:-1])
    for j in range(downPage[i]):
        count = count + 1
        url = src + downID[count-1][0]
        path = root + "第{}集.mp4".format(j+1)
        #print(url)
        #print(path)
        if not os.path.exists(root):
           os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url, stream=True)
            r.raise_for_status()
            size = int(r.headers['Content-Length'])/1024
            with open(path,'wb') as f:
               print("下载文件大小是：", size,"KB,开始下载——————————》》》")
               for i in tqdm(iterable=r.iter_content(chunk_size=1024), total=size, unit='KB', desc=infolist[i][2][7:-1] + "第{}集".format(j+1)): 
                   f.write(i)
            print("下载完毕")
        else:
           print("文件保存失败")
