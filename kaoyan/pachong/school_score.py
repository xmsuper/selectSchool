import urllib.request
import json
from pymysql import Connection
import time
import threading

def create_request(school_id):
    base_url='https://static.kaoyan.cn/json/score/2022/'
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.2.300'
    }
    for i in range(64):
        page=1
        url=base_url+str(school_id)+'/1/'+str(i+page)+'.json'
        print(url)
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        obj = json.loads(content)
        print(obj)
        time.sleep(100)

# def get_content(request):
#     response=urllib.request.urlopen(request)
#     content=response.read().decode('utf-8')
#     obj=json.loads(content)
#     return obj
def select_sql():
    conn=Connection(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        db='graduateschool'
    )
    sql='select school_id from school_info'
    cursor=conn.cursor() #获取到游标对象
    cursor.execute(sql)
    result=cursor.fetchall()
    # 元组
    print(result)
    conn.close()
    return result


def save_sql(i,sql):
    conn=Connection(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        db='graduateschool'
    )
    cursor=conn.cursor() #获取到游标对象
    cursor.execute(sql)
    conn.commit()
    conn.close()
if __name__=='__main__':
    school_id_trup=select_sql()
    for i in school_id_trup:
        create_request(i[0])