import time
from selenium import webdriver
import json

view_page_path = 'https://blog.csdn.net/weixin_39274659'
Chromedriver_path = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'


def view_increase(batch):
    with open('cookies.json', 'r') as f:
        cookie_list = json.load(f)
    print('cookie loaded')
    # 下列设置让浏览器不弹出，不影响正常电脑使用
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(Chromedriver_path, options=chrome_options)
    driver.get(view_page_path)
    driver.delete_all_cookies()
    for cookie in cookie_list:
        driver.add_cookie(cookie)
    driver.get(view_page_path)
    for i in range(batch):
        # 点击你的第一篇文章，可以自己改为你想点击文章的xpath
        driver.find_element_by_xpath('//*[@id="mainBox"]/main/div[2]/div[2]/h4/a').click()
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        # 放慢刷新次数，因为半分钟内同一ip只统计一次
        time.sleep(10)
        driver.close()
        time.sleep(10)
        driver.switch_to.window(windows[0])
        driver.refresh()
    driver.quit()


# 为防止网站监测，每刷batch次之后重启chrome driver，重新加载cookie
# count代表重启次数 batch代表每次重启刷几次网页
count = 0
batch = 2
while True:
    view_increase(batch)
    count += 1
    print('已经刷了' + str(count * batch) + '次')
    # 挂机就完事儿了
