from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pymysql import Connection
from selenium.webdriver.common.by import By
import time
import json
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

def VisitUrl(school_id):
    # 访问网站
    baseURL = "https://static.kaoyan.cn/json/school/" + str(school_id) + "/planSpecial.json"
    print(baseURL)
    return baseURL

def get_spe(school_id):
    flag=True
    try:
        pre=browser.find_element(By.XPATH,'/html/body/pre')
        flag=True
    except:
        flag=False
    if flag:
        pre=browser.find_element(By.XPATH,'/html/body/pre').text
        obj=json.loads(pre)
        data = obj['data']['master_degree']
        if len(data) == 0:
            print('空')
        else:
            print(data)
            for k, v in enumerate(data):
                # print(k,v)
                depart_id = v['depart_id']
                depart_name = v['depart_name']
                for a, b in enumerate(v['special_list']):
                    special_name = b['name']
                    special_code = b['code']
                    special_id = b['spe_id']
                    conn = Connection(
                        host="localhost",
                        port=3306,
                        user="root",
                        password="123456",
                        db='graduateschool'
                    )
                    cursor = conn.cursor()  # 获取到游标对象
                    sql = "insert into shuoshizhuanye(school_id,depart_id,depart_name,special_name,special_code,sepcial_id) values(" + str(
                        school_id) + \
                          "," + str(depart_id) + ",'" + depart_name + "','" + special_name + "','" + str(
                        special_code) + "'," + str(special_id) + ")"
                    print(sql)
                    cursor.execute(sql)
                    conn.commit()
                    conn.close()
    else:
        print('无数据')

if __name__ == '__main__':
    select_id=select_sql()
    for k,v in enumerate(select_id):
        url=VisitUrl(v[0])
        browser.get(url)
        print('正在打印第'+str(k+1)+'个学校')
        get_spe(v[0])
        print('第'+str(k+1)+'个学校获取成功\n\n\n')
