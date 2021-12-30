import  requests
import  re

import imageio
import jieba
from wordcloud import wordcloud




url = "https://api.bilibili.com/x/v1/dm/list.so?oid=471745018"
requests = requests.get(url)
requests.encoding = 'utf-8'
requests = requests.text
pattern = re.compile('<d.*?>(.*?)</d>')
data = pattern.findall(requests)

with open('danmu.txt','w',newline='',encoding='utf-8') as f :
    for i in data:
        f.write(i)
        f.write("\n")





mk = imageio.imread("img_2.png")
w = wordcloud.WordCloud(mask=mk)

# 构建并配置词云对象w，注意要加scale参数，提高清晰度
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc',
                        mask=mk,
                        scale=20)

# 对来自外部文件的文本进行中文分词，得到string
f = open('danmu.txt',encoding='utf-8')
txt = f.read()
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出到当前文件夹
w.to_file('danmu.png')





