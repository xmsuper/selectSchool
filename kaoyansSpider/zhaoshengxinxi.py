import json
import time
import urllib.request
# https://static.kaoyan.cn/json/school/5/planSpecial.json  双一流建设
import random
from pymysql import Connection

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
def syl_build(school_id):
    proxies_pool = [
        {'http': '121.13.252.62'},
        {'http': '222.74.73.202'},
        {'http': '210.5.10.87'},
        {'http': '183.236.232.160'},
        {'http': '121.13.252.58'},
        {'http':'61.216.185.88'},
        {'http':'117.94.119.75'},
        {'http':'202.109.157.60'},
        {'http': '182.139.111.68'},
        {'http': '182.139.110.18'},
        {'http': '182.139.110.36'},
    ]
    proxies = random.choice(proxies_pool)
    print(proxies)
    baseURL="https://static.kaoyan.cn/json/school/"+str(school_id)+"/planSpecial.json"
    headers = {
        'access-control-allow-origin':'https://www.kaoyan.cn',
        'content-encoding': 'gzip',
        'content-md5': 'NXvcF1l9ia+1j+e06V4dSQ==',
        'content-type': 'application/json',
        'last-modified': 'Wed, 08 Mar 2023 05:58:23 GMT',
        'server': 'AliyunOSS',
        'vary': 'Accept-Encoding',
        'x-oss-hash-crc64ecma': '13205611798106383243',
        'x-oss-object-type': 'Normal',
        'x-oss-request-id': '640834D065F7E53433B60485',
        'x-oss-server-time': '33',
        'x-oss-storage-class': 'Standard',
        'x-ser': 'BC138_dx-lt-yd-zhejiang-huzhou-3-cache-5, BC10_lt-jiangsu-lianyungang-8-cache-5',
    }
    request=urllib.request.Request(url=baseURL,headers=headers)
    handler=urllib.request.ProxyHandler(proxies=proxies)
    opener=urllib.request.build_opener(handler)
    return request,opener
def get_content(request,opener,school_id):
    # response=urllib.request.urlopen(request)
    response=opener.open(request)
    # print(response)
    content=response.read().decode('utf-8')
    obj = json.loads(content)
    syl_jianshe=obj["data"]["syl_jianshe"]
    print(syl_jianshe)
    # str1=''
    # for i in syl_jianshe:
    #     str1=str1+i+"  "
    # conn = Connection(
    #     host="localhost",
    #     port=3306,
    #     user="root",
    #     password="123456",
    #     db='graduateschool'
    # )
    # cursor = conn.cursor()  # 获取到游标对象
    # sql="insert into syl_build(school_id,syl_jianshe) values " \
    #     "("+str(school_id)+",'"+str1+"')"
    # print(sql)
    # cursor.execute(sql)
    # conn.commit()
    # conn.close()

if __name__=='__main__':
    select_id=select_sql()
    for k,v in enumerate(select_id):
        request, opener = syl_build(v[0])
        print("正在打印第"+str(k+1)+'个')
        get_content(request,opener,v[0])
        print("第"+str(k+1)+'个获取成功'+'\n')
        # time.sleep(2)
