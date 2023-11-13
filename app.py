# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 12:14:45 2022

@author: Phoenix
"""
import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,QuickReply,MessageAction,QuickReplyButton
)

app = Flask(__name__)

line_bot_api = LineBotApi('pVqQlOC3JfOAV2UBlCZjqXzDRl6MRIut3oB22UOVwcz7/a4Wz9oc0nk+hlzLs7RzDvS9QYKCWPCSSSNJpyQR39Js7hbTUNENGnfNEys69OJIdhb9+pJQMTy3QfnwZIGBRTqQJ0FbzCiPbA2TZMar0AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9015e07eb414aee62893df4fca5e6f16')

def ptt(link):
    import urllib.request as req 
    import bs4
    end=''
    url=link
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("span",class_="push-tag")[-26:]
    comment=root.find_all("span",class_="f3 push-content")[-26:]
    user=root.find_all("span",class_="push-userid")[-26:]
    time=root.find_all("span",class_="push-ipdatetime")[-26:]
    for c,f,e,g in zip(titles,user,comment,time):
        dd=str(c.string) + str(f.string) + str(e.string) + str(g.string)
        end += dd
        end +="\n"

    return end

def holox(holo):
    
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.keys import Keys
    from bs4 import BeautifulSoup
    from selenium.webdriver.common.by import By
    result=""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.getenv("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless") #無頭模式
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.getenv("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    # driver = webdriver.Chrome(r'C:\Users\Phoenix\Desktop\chromedriver.exe')
    

    # options.add_argument("--headless")

    driver.get('https://www.google.com.tw/imghp?hl=zh-TW&authuser=0&ogbl')
    driver.find_element(By.NAME,'q').send_keys(holo)
    
    driver.find_element(By.CLASS_NAME,'Tg7LZd').click()

    sleep(2)
    for i in range(0,5):
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
        sleep(1)

    the_d=driver.find_elements(By.CLASS_NAME,'bRMDJf,islir')

    for d in the_d:
        
        d.click()
        
        sleep(5)
        # image=driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img')
        soup = BeautifulSoup(driver.page_source,'html.parser')
        website=soup.select('#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id > div > a > img[src^=http]')
        for i in website:
            website=i.get('src')
        result=('{}'.format(website))
        sleep(3)
        driver.quit()
        return result
        
    
    # url = soup.select('div.title a[href^="/bbs"]')
    
def lotto(y,m):
    import requests
    from bs4 import BeautifulSoup
    import re
    result=""

    my_header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}

    r = requests.get('https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx',headers = my_header)
    if r.status_code == 200:
        # print(r.text)
        soup = BeautifulSoup(r.text,'html.parser')
        __VIEWSTATE = soup.find('input',id="__VIEWSTATE").get('value')
        __VIEWSTATEGENERATOR = soup.find('input',id="__VIEWSTATEGENERATOR").get('value')
        __EVENTVALIDATION = soup.find('input',id="__EVENTVALIDATION").get('value')

    for year in range(103,int(y)+1):
        for month in range(1,int(m)+1):      
            my_data={'__VIEWSTATE': __VIEWSTATE,
                      '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
                      '__EVENTVALIDATION': __EVENTVALIDATION,
        
                      'forma': '請選擇遊戲',
                      'SuperLotto638Control_history1$txtNO': '',
                      'SuperLotto638Control_history1$chk': 'radYM',
                      'SuperLotto638Control_history1$dropYear': year,
                      'SuperLotto638Control_history1$dropMonth': month,
                      'SuperLotto638Control_history1$btnSubmit': '查詢',
            }
        
            r = requests.post('https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx',headers = my_header, data = my_data)
            if r.status_code == 200:
                # print(r.text)
                soup = BeautifulSoup(r.text,'html.parser')
                
                nums = soup.find_all('span', id = re.compile('SuperLotto638Control_history1_dlQuery_SNo\d_\d'))
                
                result += str(year) +" " + str(month) + "\n"
                for index,num in enumerate(nums):
                    # print(num.text,end=' ')
                    result += num.text +" "
                    if (index+1) % 7 ==0:
                        # print()
                        result +="\n"
                # print("--------------------------------------")
                result += "---------------------------------------" + "\n"
    return result  
def eat():
    result = '生魚片'
    return result 

def work():
    import csv
    import numpy as np
    listt =[]
    result=''
    with open("work.csv",encoding=("Big5")) as work:
        data =csv.reader(work)
        listdata =np.array(list(data))

        date=listdata[1][3:-2]

        sunday=listdata[2][3:-2]

        wwork=listdata[16][3:-2]
    for b,c,d in zip(date,sunday,wwork):
        listt.append(b)
        listt.append(c)
        listt.append(d)

    result += str(listt)
    return result
def work2():
    import csv
    import numpy as np
    listt =[]
    result=''
    with open("work.csv",encoding=("Big5")) as work:
        data =csv.reader(work)
        listdata =np.array(list(data))

        date=listdata[26][1:32]

        sunday=listdata[27][1:32]

        wwork=listdata[28][1:32]
    for b,c,d in zip(date,sunday,wwork):
        listt.append(b)
        listt.append(c)
        listt.append(d)

    result += str(listt)
    return result

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

item1 =[
    QuickReplyButton(action=MessageAction(label="仁愛15", text="仁愛15")),
    QuickReplyButton(action=MessageAction(label="仁愛13", text="仁愛13")),
    QuickReplyButton(action=MessageAction(label="數據2", text="數據2")),
    QuickReplyButton(action=MessageAction(label="數據OC", text="數據OC")),
    QuickReplyButton(action=MessageAction(label="數據3B", text="數據3B")),

]

item2 =[
    QuickReplyButton(action=MessageAction(label="數據3B", text="數據3B")),
    QuickReplyButton(action=MessageAction(label="數據3L", text="數據3L")),
    QuickReplyButton(action=MessageAction(label="數據3A", text="數據3A")),
    QuickReplyButton(action=MessageAction(label="數據3R", text="數據3R")),
    QuickReplyButton(action=MessageAction(label="仁愛15", text="仁愛15")),  

] 

def holo(vtuber):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    developerKey = os.getenv('apikey')
    youtube = build('youtube', 'v3',
                    developerKey=developerKey)
    request = youtube.search().list(
        part="snippet",
        eventType="live",
        q=vtuber,
        type="video"
    )
    response = request.execute()

    return response
def holo_search(vtuber):   
    
    try:
        search_response=holo(vtuber)
        for item in search_response['items']:
            # 提取频道的信息
            # channel_id = item['id']['channelId']  # 频道ID
            video_id = item['id']['videoId']
            channel_title = item['snippet']['title']  # 频道标题
            channel_description = item['snippet']['description']  # 频道描述
            
            title=f'頻道標題: {channel_title}"\n"'
            description = f'頻道描述: {channel_description}"\n"'
            link= f'https://www.youtube.com/watch?v={video_id}'

            
        result = title+description+link
        return result
    
    except HttpError as e:
        result = f'：{e}'
        return result 
@app.route("/")
def index():
    return "Hello, World!"
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #print("Handle: reply_token: " + event.reply_token + ", message: " + event.message.text)
    # content = "{}: {}".format('Hello World', event.message.text)
    p=("{}".format(event.message.text))
    c=p.upper()
    if  "SEARCH"in c :
        holo=event.message.text.split("@")[1]
        content =holox(holo)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(original_content_url=content,
                             preview_image_url=content))
        
    elif 'HTTP' in c :
        link=event.message.text
        content = ptt(link)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
    elif '吃啥' in c :
        content =eat()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
    elif '下月班表' == c :
        content =work2()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))

    elif '假表' == c :
        content =work()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
    elif 'HOLO@' in c :
        vtuber = event.message.text.split("@")[1]
        content =holo_search(vtuber)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
    elif '機房' in c or '仁愛' in c :
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
            text="請選擇機房:",
            quick_reply=QuickReply(items=item1)      ))  

    elif '數據3' in c :
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
            text="請選擇機房:",
            quick_reply=QuickReply(items=item2)      ))       

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ.get('PORT', 5000))
    #9*9    
    #     a=event.message.text.split("@")[0]
    #     b=event.message.text.split("@")[1]
        
    #     content =""
    #     for r in range(1,int(a)+1):
    #         for c in range(1,int(b)+1):
    #             # print(str(r)+"*"+str(c)+"="+str(r*c))
    #             content += str(r) + "*" + str(c) +"=" +str(r*c)+" "
    #         content += "\n"
    #lotto
    # year=int(event.message.text.split("@")[0])
    # month=int(event.message.text.split("@")[1])    
    # content=lotto(year,month)