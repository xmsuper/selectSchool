import json
import urllib.request
from pymysql import Connection

url='https://static.kaoyan.cn/json/rank/ai_rec_school.json'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.1.301'
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
data=json.loads(content)
hotSearch=data['data']
for i in hotSearch:
    conn = Connection(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        db='graduateschool'
    )
    cursor = conn.cursor()  # 获取到游标对象
    sql='insert into hotsearchschool(school_id,school_name) values ("'+str(i['school_id'])+'","'+str(i['school_name'])+'")'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
print('插入完毕')