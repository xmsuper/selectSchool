import json
import urllib.request
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


def accept_sql(id):
    # from pymysql import Connection
    url = 'https://static.kaoyan.cn/json/school/' + str(id) + '/info.json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.1.301'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    data = json.loads(content)
    school_data=data['data']
    school_intro=(school_data['intro']).replace("'","\"")
    # print(school_intro)
    # school_intro.replace("'","\"")
    # print(school_intro)
    conn = Connection(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        db='graduateschool'
    )
    cursor = conn.cursor()  # 获取到游标对象
    sql = "insert into school_detail(school_id,belongsTo,create_date,intro,num_doctor,num_lab,num_master,num_subject,school_space)"\
          """values("""+str(school_data["school_id"])+""",'"""+school_data['belongsTo']+"""',"""+str(school_data['create_date'])+""",'"""+school_intro+"""',"""+str(school_data['num_doctor'])+""","""+str(school_data['num_lab'])+""","""+str(school_data['num_master'])+""","""+str(school_data['num_subject'])+""",'"""+str(school_data['school_space'])+""""')"""
    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('插入成功')



if __name__ == '__main__':
    select_id = select_sql()
    for k,v in enumerate(select_id):
        print('正在打印第'+str(k+1)+'个')
        accept_sql(v[0])