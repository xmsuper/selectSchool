import time
import urllib.request
# 导入selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from pyautogui import position
import pyautogui
from pymysql import Connection


path=Service('chromedriver.exe')
browser=webdriver.Chrome(service=path)
browser.maximize_window()
def select_sql():
    conn = Connection(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        db='graduateschool'
    )
    cursor = conn.cursor()  # 获取到游标对象
    sql = 'select school_id from school_info'
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    return results


# 请求
def VisitUrl(schoolID):
    # 访问网站
    baseUrl='https://www.kaoyan.cn/school/'
    url =baseUrl+str(schoolID)+'/score'
    print(url)
    return url

name = ''

# 专业型硕士
def getProfessionalScore():
    schoolName=browser.find_element(By.XPATH,'//span[@class="school-header_name__Gx3Qm"]').text
    schoolWeb=browser.find_element(By.XPATH,'//span[@class="school-header_url__GKaKd"]').text
    schoolTel=browser.find_element(By.XPATH,'//span[@class="school-header_phone___GdHM"]').text
    schoolEmail=browser.find_element(By.XPATH,'//span[@class="school-header_emil__3GrJV"]').text
    pageNumbers=browser.find_elements(By.XPATH,'//li[@title]/a')
    if len(pageNumbers)>0:
        for i in range(len(pageNumbers)):
            schoolScore = browser.find_elements(By.XPATH, '//tr/td')
            list=[]
            for l in schoolScore:
                list.append(l.text)
                if len(list)==9:
                    conn = Connection(
                        host="localhost",
                        port=3306,
                        user="root",
                        password="123456",
                        db='graduateschool'
                    )
                    cursor = conn.cursor()  # 获取到游标对象
                    sql = 'insert into school_score(school_name,school_tel,school_web,school_email,learnType,major_code,major_name,total,politics,english,procourse,procourese2,remark) ' \
                          'values("' +schoolName + '","' + schoolTel + '","' + schoolWeb + '","' + schoolEmail + '","' + list[
                              0] + '","' + list[1] + '","' + list[2] + '","' + list[3] + '","' + list[4] + '","' + list[5] + '","' + list[6] + '","' + list[7] + '","' + list[8] + '")'
                    print(sql)
                    cursor.execute(sql)
                    conn.commit()
                    conn.close()
                    list.clear()

            if (i+1)!=len(pageNumbers):
                time.sleep(3)
                nextButton = browser.find_element(By.XPATH, '//li[@title="下一页"]')
                nextButton.click()
                time.sleep(1)
    else:
        schoolScore = browser.find_elements(By.XPATH, '//tr/td')
        list = []
        for l in schoolScore:
            list.append(l.text)
            if len(list) == 9:
                conn = Connection(
                    host="localhost",
                    port=3306,
                    user="root",
                    password="123456",
                    db='graduateschool'
                )
                cursor = conn.cursor()  # 获取到游标对象
                sql = 'insert into school_score(school_name,school_tel,school_web,school_email,learnType,major_code,major_name,total,politics,english,procourse,procourese2,remark) ' \
                      'values("' + schoolName + '","' + schoolTel + '","' + schoolWeb + '","' + schoolEmail + '","' + \
                      list[
                          0] + '","' + list[1] + '","' + list[2] + '","' + list[
                          3] + '","' + list[4] + '","' + list[5] + '","' + list[6] + '","' + list[7] + '","' + list[
                          8] + '")'
                print(sql)
                cursor.execute(sql)
                conn.commit()
                conn.close()
                list.clear()
# 获取学术型硕士分数
def academicScore():
    schoolName = browser.find_element(By.XPATH, '//span[@class="school-header_name__Gx3Qm"]').text
    schoolWeb = browser.find_element(By.XPATH, '//span[@class="school-header_url__GKaKd"]').text
    schoolTel = browser.find_element(By.XPATH, '//span[@class="school-header_phone___GdHM"]').text
    schoolEmail = browser.find_element(By.XPATH, '//span[@class="school-header_emil__3GrJV"]').text
    # 查找专业型硕士按钮 先点击选项按钮
    professionalBtn = browser.find_elements(By.XPATH, '//div[@title="专业型硕士"]')
    if len(professionalBtn)>0:
        professionalBtn[0].click()
        time.sleep(3)
        x, y = position()
        # 点击学士型硕士
        pyautogui.click(1031, 441)
        time.sleep(1)
        pageNumbers=browser.find_elements(By.XPATH,'//li[@title]/a')
        for i in range(len(pageNumbers)):
            schoolScore = browser.find_elements(By.XPATH, '//tr/td')
            list=[]
            for l in schoolScore:
                list.append(l.text)
                if len(list)==9:
                    conn = Connection(
                        host="localhost",
                        port=3306,
                        user="root",
                        password="123456",
                        db='graduateschool'
                    )
                    cursor = conn.cursor()  # 获取到游标对象
                    sql = 'insert into school_score(school_name,school_tel,school_web,school_email,learnType,major_code,major_name,total,politics,english,procourse,procourese2,remark) ' \
                          'values("' +schoolName + '","' + schoolTel + '","' + schoolWeb + '","' + schoolEmail + '","' + list[
                              0] + '","' + list[1] + '","' + list[2] + '","' + list[
                              3] + '","' + list[4] + '","' + list[5] + '","' + list[6] + '","' + list[7] + '","' + list[8] + '")'
                    print(sql)
                    cursor.execute(sql)
                    conn.commit()
                    conn.close()
                    list.clear()
            if (i+1)!=len(pageNumbers):
                time.sleep(3)
                nextButton = browser.find_element(By.XPATH, '//li[@title="下一页"]')
                nextButton.click()
                time.sleep(1)
if __name__ == '__main__':
    select_id=select_sql()
    for i in select_id:
        url=VisitUrl(i[0])
        browser.get(url)
        time.sleep(3)
        res1=getProfessionalScore()
        res2=academicScore()
        print(name,res1,res2)
#获取网页源码
# content=browser.page_source
# print(content)
# 根据id找到对象
# for i in range(10):


