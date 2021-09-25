import requests
from bs4 import BeautifulSoup
import smtplib
import time

def check_price():
    r = requests.get("https://www.ikea.com.tw/zh/products/sofas/sofas/gronlid-spr-39256293" )
    soup = BeautifulSoup(r.content, "html.parser")
    title = soup.find("h1", class_="itemFacts font-weight-normal").get_text().replace("\n", " ").strip()
    price = soup.find("p", class_="itemNormalPrice display-6").get_text().replace(",", "").replace("$","").strip()
    price = int(price)

    if price < 15000:
        print(price)
        send_mail(price)

def send_mail(price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # https://myaccount.google.com/security 
    # Gmail 帳號要開啟"兩段式驗證", 這樣產生的"專用密碼"才能讓我們的 Python 應用程式"避開兩段式驗證"發送信件
    server.login("molly6825@gmail.com", "gbcyvodmrkleijuo")
    
    subject = "Price fell down"
    body = f"Check the Ikea product link: https://www.ikea.com.tw/zh/products/sofas/sofas/gronlid-spr-39256293 \n {price}" 
    # 格式必須長這樣 前面是subject 空兩行寫內文
    msg = f"Subject: {subject}\n\n{body}"
    # server.sendmail(from add, to add, msg)
    # sendmail() 不能傳送中文，因此若是產品名稱是中文，無法傳送到email
    server.sendmail(
        "molly6825@gmail.com",
        "molly6825@gmail.com",
        msg
    )

    print("Email has been sent")

    server.quit()

while 1:
    check_price()
    time.sleep(60*60)


# 自訂表頭
# my_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

# 將自訂表頭加入 GET 請求中
# r = requests.get('http://httpbin.org/get', headers = my_headers)

# soup.find() 的不同寫法
# soup.find(id='p2') 回傳第一個 id="p2" 的區塊
# soup.find('p', id='p2') 回傳第一個被 <p> </p> 所包圍的區塊且 id="p2"
# soup.find('h1', 'large') 找尋第一個 <h1> 區塊且 class="large"
# soup.find('h1', class_ ='large') 同上


# tag定位之後，我們就可以更進一步想要抓自己想要的資訊
# tag.get_text() 回傳str

# str.strip() "預設"去除字串頭尾的"空格":
# str = "0000000   jb51.net 0000000"
# print(str.strip( '0' )) # 去除首尾字元 0 
# str2 = "  jb51.net   "  
# print(str2.strip())     # 去除首尾空格

# [number]取得字串內的部分字元 ex: the_word[0:5] 可以取得第0個index到第4個index的字元

# import time
# time.sleep(sec) 推遲幾秒後再動作

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.ehlo()
# server.starttls()

# msg 字串須以 "Subjects:" 開頭, 它後面跟的字串就會被當作信件"主旨", 直到兩個 "\n" 出現，後面接續 "內文body"
