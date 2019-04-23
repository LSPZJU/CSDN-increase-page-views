import time
from selenium import webdriver
import json

view_page_path = 'https://blog.csdn.net/weixin_39274659'
Chromedriver_path = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'

browser = webdriver.Chrome(Chromedriver_path)
browser.get(view_page_path)
# 在暂停时间内快速登录账号(如微信扫码)，然后等待cookie下载
time.sleep(10)
cookie_list = browser.get_cookies()
print(cookie_list)
jsonCookies = json.dumps(cookie_list)
with open('cookies.json', 'w') as f:
    f.write(jsonCookies)
print('saving cookies completes')

browser.close()
browser.quit()
