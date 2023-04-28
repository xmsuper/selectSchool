from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pymysql import Connection
from selenium.webdriver.common.by import By
import time

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
def VisitUrl(schoolID):
    # 访问网站
    baseUrl='https://www.kaoyan.cn/school/'
    url =baseUrl+str(schoolID)+'/major'
    print(url)
    return url
def get_syl_jianshe(school_id):
    flag=True
    flag2 = True
    try:
        syl_title=browser.find_element(By.XPATH,'//p[@class="school-page-major_title__2W1xH"]')
        flag=True
        try:
            find_more=browser.find_element(By.XPATH, '//div[@class="school-page-major_fold__14HqV"]')
            flag2=True
        except:
            flag2=False
    except:
        flag=False
        flag2 =False
    print(flag2)
    if flag:
        print('有双一流')
        if flag2:
            find_more=browser.find_element(By.XPATH, '//div[@class="school-page-major_fold__14HqV"]')
            find_more.click()
            syl = browser.find_elements(By.XPATH, '//p[@class="school-page-major_majorDoubleTitle__39nC8"]')
            str1 = ''
            for l in syl:
                str1 = str1 + l.text + '  '
            print(str1+"\n\n\n")
            conn = Connection(
                host="localhost",
                port=3306,
                user="root",
                password="123456",
                db='graduateschool'
            )
            cursor = conn.cursor()  # 获取到游标对象
            sql = "insert into syl_build(school_id,syl_jianshe) values (" + str(school_id) + ",'" + str1 + "')"
            print(sql)
            cursor.execute(sql)
            conn.commit()
            conn.close()
        else:
            syl = browser.find_elements(By.XPATH, '//p[@class="school-page-major_majorDoubleTitle__39nC8"]')
            str1 = ''
            for l in syl:
                str1 = str1 + l.text + '  '
            print(str1+"\n\n\n")
            conn = Connection(
                host="localhost",
                port=3306,
                user="root",
                password="123456",
                db='graduateschool'
            )
            cursor = conn.cursor()  # 获取到游标对象
            sql = "insert into syl_build(school_id,syl_jianshe) values (" + str(school_id) + ",'" + str1 + "')"
            print(sql)
            cursor.execute(sql)
            conn.commit()
            conn.close()
    else:
        print('没有双一流')
        conn = Connection(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
            db='graduateschool'
        )
        cursor = conn.cursor()  # 获取到游标对象
        sql = "insert into syl_build(school_id,syl_jianshe) values (" + str(school_id) + ",'null')"
        print(sql)
        cursor.execute(sql)
        conn.commit()
        conn.close()

if __name__ == '__main__':
    select_id=select_sql()
    for k,v in enumerate(select_id):
        url=VisitUrl(v[0])
        browser.get(url)
        get_syl_jianshe(v[0])
        # time.sleep(2)
        # print(get_syl_jianshe(v[0]))