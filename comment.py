import csv

from selenium import webdriver
import  time

driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.get("https://www.bilibili.com/video/BV1ML411j7au?spm_id_from=333.851.b_7265636f6d6d656e64.1")

#获取页面初始高度
js = 'return action=document.body.scrollHeight'
height = driver.execute_script(js)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(3)
t1 = int(time.time())
status = True
num = 0

while status:
    t2 = int(time.time())
    if t2-t1<30:
        new_height = driver.execute_script(js)
        if new_height > height:
            time.sleep(1)
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            #重置初始页面高度
            height = new_height
            #重置时间戳.重新计时
            t1 = int(time.time())

    elif num < 3:
        time.sleep(3)
        num = num+1

    else:
        print("滚动条已经处于页面最底部")
        status = False
        driver.execute_script('window.scrollTo(0,0)')
        break


data = []

commentElement = driver.find_elements_by_xpath('//p[@class="text"]')
text = [i.text for i in commentElement]
data.append(text)

with open("./commentList.csv","a",encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile,delimiter='\n')
    writer.writerow(map(lambda i: [i],data))

























