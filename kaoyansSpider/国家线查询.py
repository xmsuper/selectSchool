# https://static.kaoyan.cn/json/query/query_gjx_score.json
import json
import urllib.request
from pymysql import Connection
url='https://static.kaoyan.cn/json/query/query_gjx_score.json'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.1.301'
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
obj=json.loads(content)
data=obj['data']
# print(data)
for i in data:
    for j in data[i]:
        # print(str(i)+'年')
        # print(j)
        conn = Connection(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
            db='graduateschool'
        )
        cursor = conn.cursor()  # 获取到游标对象
        sql='insert into countryLine(id,school_year,code,major_name,total,single_100,single_150,degree_type,area_type) values ' \
            '('+str(j['id'])+','+str(j['year'])+',"'+str(j['code'])+'","'+j['name']+'",'+str(j['total'])+','+\
            str(j['single_100'])+','+str(j['single_150'])+','+str(j['degree_type'])+',"'+j['area_type']+'")'
        print(sql)
        cursor.execute(sql)
        conn.commit()
        conn.close()