from splinter import Browser
import time
#selenium之 chromedriver与chrome版本映射表（更新至v2.43）
#https://blog.csdn.net/huilan_same/article/details/51896672
#chromedriver 下载地址
#http://npm.taobao.org/mirrors/chromedriver/
#安装到chrome和python的安装目录下，设置path环境变量


def main():
    browser= Browser(driver_name="chrome")
    browser.visit("https://www.baidu.com")
    browser.fill('wd','百家号')
    time.sleep(1)
    button=browser.find_by_id("su")
    button.click()
    while true:
        pass

if __name__=='__main__':
    main()