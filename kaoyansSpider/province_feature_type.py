import urllib.request
import json
from pymysql import Connection
def create_request():
    url='https://static.kaoyan.cn/json/query/query_school.json'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.1.301'
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    obj=json.loads(content)
    data=obj['data']
    return data

def feature(data):
    feature=data['feature']
    print(feature)
    for i in feature:
        i.update({"type": "feature"})
        save_sql(i)
def type(data):
    type=data['type']
    print(type)
    for i in type:
        i.update({"type":"school_type"})
        save_sql(i)
def province_A(data):
    province_id=data['province_id']
    list=province_id['A']
    for province_a in list:
        province_a.update({"type":"province_a"})
        # save_sql(province_a)
def province_B(data):
    province_id=data['province_id']
    list=province_id['B']
    for province_b in list:
        province_b.update({"type":"province_b"})
        # save_sql(province_b)
def province_Other(data):
    province_id=data['province_id']
    list=province_id['other']
    for province_other in list:
        province_other.update({"type":"province_other"})
        # save_sql(province_other)


def save_sql(i):
    conn=Connection(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        db='graduateschool'
    )
    cursor=conn.cursor() #获取到游标对象
    sql='insert into'+' '+i['type']+'(code,name,type) values("'+i['code']+'","'+i['name']+'","'+i['type']+'")'
    cursor.execute(sql)
    conn.commit()
    conn.close()
if __name__=='__main__':
    requests=create_request()
    content=get_content(requests)
    province_A(content)
    province_B(content)
    province_Other(content)
    feature(content)
    type(content)
