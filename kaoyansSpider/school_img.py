import time
import urllib.request
# 导入selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from pyautogui import position
import pyautogui
from pymysql import Connection
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def share_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    # path是你自己浏览器的路径
    path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location=path
    browser=webdriver.Chrome(chrome_options=chrome_options)
    return browser
browser=share_browser()
url='https://www.kaoyan.cn/school'
browser.get(url)
i = 1
while i<=107:
    i+=1
    print(i)
    school_name = browser.find_elements(By.XPATH, '//span[@class="school-list-item_name___f-cs"]')
    school_img = browser.find_elements(By.XPATH, '//div[@class="school-list-item_img__2H5Ny"]/img')
    for i in range(len(school_img)):
        list=[]
        list.append(school_name[i].text)
        list.append(school_img[i].get_attribute('src'))
        conn = Connection(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
            db='graduateschool'
        )
        cursor = conn.cursor()  # 获取到游标对象
        # sql = 'insert into school_img(school_name,school_img) values("'+list[0]+'","'+list[1]+'")'
        sql='update school_img set school_img="'+list[1]+'" where school_name="'+list[0]+'"'
        print(sql)
        cursor.execute(sql)
        conn.commit()
        conn.close()
        list.clear()
    time.sleep(2)
    nextBtn=browser.find_element(By.XPATH,'//li[@title="下一页"]')
    s = nextBtn.get_attribute('aria-disabled')
    if s=='false':
        nextBtn.click()
        time.sleep(1)
    else:
        i=200


'//div[@class="school-list-item_img__2H5Ny"]/img/@src'
'//span[@class="school-list-item_name___f-cs"]'
'//li[@class=" ant-pagination-next"]/@aria-disabled'
'//span[@class="school-list-item_name___f-cs"]'