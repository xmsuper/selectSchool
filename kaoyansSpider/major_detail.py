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
    sql = 'select a.school_id,b.depart_id,b.sepcial_id  from school_info as a left join shuoshizhuanye as b on a.school_id=b.school_id'
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    return results

def VisitUrl(school_id,depart_id,special_id):
    # 访问网站
    baseURL = "https://static.kaoyan.cn/json/school/"+str(school_id)+"/depart/"+str(depart_id)+"/special/"+str(special_id)+"/specialInfo.json"
    print(baseURL)
    return baseURL

def get_info(school_id,depart_id,special_id):
    pre=browser.find_element(By.XPATH,'/html').text
    obj = json.loads(pre)
    data = obj['data']
    major_data=data['switchArr']
    if len(data['switchArr'])==2:
        for k,v in enumerate(data['switchArr']):
            recruit_name=v['recruit_name']
            special_name=v['special_name']
            special_code=v['special_code']
            school_name=v['info']['school_name']
            depart_name=v['info']['depart_name']
            year=v['info']['year']
            recruit_type=v['info']['recruit_type']
            level1=v['info']['level1']
            level1_code=v['info']['level1_code']
            level2=v['info']['level2']
            level2_code=v['info']['level2_code']
            recruit_number=v['info']['recruit_number']

            subject_name1=v['subject'][0]['name']
            str1=v['subject'][0]['value']
            subject1=str1.replace("'","").replace("\n","")

            subject_name2=v['subject'][1]['name']
            str2=v['subject'][1]['value']
            subject2=str2.replace("'","")

            subject_name3=v['subject'][2]['name']
            str3=v['subject'][2]['value']
            subject3=str3.replace("'","")
            conn = Connection(
                host="localhost",
                port=3306,
                user="root",
                password="123456",
                db='graduateschool'
            )
            cursor = conn.cursor()  # 获取到游标对象
            sql="insert into major_detail(school_id,depart_id,special_id,recruit_name,special_name,special_code" \
                ",school_name,depart_name,year,recruit_type,level1,level1_code,level2," \
                "level2_code,recruit_number,subject_name1,subject1,subject_name2,subject2," \
                "subject_name3,subject3) values("+str(school_id)+","+str(depart_id)+","+str(special_id)+\
                ",'"+recruit_name+"','"+special_name+"','"+special_code+"','"+school_name+"','"+depart_name+"',"+str(year)+",'"+recruit_type+"','"+level1+"','"+level1_code+"','"+level2+"','"+level2_code+\
                "',"+str(recruit_number)+",'"+subject_name1+"','"+subject1+"','"+subject_name2+"','"+subject2+"','"+subject_name3+"','"+subject3+"')"
            print(sql)
            cursor.execute(sql)
            conn.commit()
            conn.close()
    else:
        recruit_name = major_data[0]['recruit_name']
        special_name = major_data[0]['special_name']
        special_code = major_data[0]['special_code']
        school_name = major_data[0]['info']['school_name']
        depart_name = major_data[0]['info']['depart_name']
        year = major_data[0]['info']['year']
        recruit_type = major_data[0]['info']['recruit_type']
        level1 = major_data[0]['info']['level1']
        level1_code = major_data[0]['info']['level1_code']
        level2 = major_data[0]['info']['level2']
        level2_code = major_data[0]['info']['level2_code']
        recruit_number = major_data[0]['info']['recruit_number']

        subject_name1 = major_data[0]['subject'][0]['name']
        str1=major_data[0]['subject'][0]['value']
        subject1 =str1.replace("'","").replace("\n","")

        subject_name2 = major_data[0]['subject'][1]['name']
        str2=major_data[0]['subject'][1]['value']
        subject2 = str2.replace("'","")

        subject_name3 = major_data[0]['subject'][2]['name']
        str3=major_data[0]['subject'][2]['value']
        subject3 =str3.replace("'","")
        conn = Connection(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
            db='graduateschool'
        )
        cursor = conn.cursor()  # 获取到游标对象
        sql = "insert into major_detail(school_id,depart_id,special_id,recruit_name,special_name,special_code" \
              ",school_name,depart_name,year,recruit_type,level1,level1_code,level2," \
              "level2_code,recruit_number,subject_name1,subject1,subject_name2,subject2," \
              "subject_name3,subject3) values(" + str(school_id) + "," + str(depart_id) + "," + str(special_id) + \
              ",'" + recruit_name + "','" + special_name + "','" + special_code + "','" + school_name + "','" + depart_name + "'," + str(year) + ",'" + recruit_type + "','" + level1 + "','" + level1_code + "','" + level2 + "','" + level2_code + \
              "'," + str(recruit_number) +",'"+ subject_name1 +"','" + subject1 + "','" + subject_name2 + "','" + subject2 + "','" + subject_name3 + "','" + subject3 + "')"
        print(sql)
        cursor.execute(sql)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    select_id=select_sql()
    for k,v in enumerate(select_id):
        url=VisitUrl(v[0],v[1],v[2])
        browser.get(url)
        print('正在打印第'+str(k+1)+'个专业')
        get_info(v[0],v[1],v[2])
        print('第'+str(k+1)+'个专业获取成功\n\n\n')
