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
    return request
def get_content(request,school_id):
    response = urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    obj = json.loads(content)
    data=obj['data']['master_degree']
    if len(data)==0:
        print('空')
    else:
        print(data)
        for k,v in enumerate(data):
            # print(k,v)
            depart_id=v['depart_id']
            depart_name=v['depart_name']
            for a,b in enumerate(v['special_list']):
                special_name=b['name']
                special_code=b['code']
                special_id=b['spe_id']
                conn = Connection(
                    host="localhost",
                    port=3306,
                    user="root",
                    password="123456",
                    db='graduateschool'
                )
                cursor = conn.cursor()  # 获取到游标对象
                sql = "insert into shuoshizhuanye(school_id,depart_id,depart_name,special_name,special_code,sepcial_id) values("+str(school_id)+\
                      ","+str(depart_id)+",'"+depart_name+"','"+special_name+"','"+str(special_code)+"',"+str(special_id)+")"
                print(sql)
                cursor.execute(sql)
                conn.commit()
                conn.close()
if __name__=='__main__':
    select_id=select_sql()
    for k,v in enumerate(select_id):
        if k+1<126:
            request= syl_build(v[0])
            print("正在打印第" + str(k + 1) + '个学校')
            get_content(request, v[0])
            print("第" + str(k + 1) + '个学校获取成功' + '\n')
        else:
            request= syl_build(v[0])
            print("正在打印第" + str(k + 1) + '个学校')
            get_content(request, v[0])
            print("第" + str(k + 1) + '个学校获取成功' + '\n')
            time.sleep(5*60)
