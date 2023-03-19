import json
import urllib.request

from pymysql import Connection


def create_request(page):
    base_url = 'https://api.kaoyan.cn/pc/school/schoolList'
    data = {
        'page': page,
        'limit': 10,  # 该接口的分页查询是由前端控制的，所以这里直接设置一个很大的值
        'province_id': '',
        'type': '',
        'feature': '',
        'school_name': ''
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.1.301'
    }
    request = urllib.request.Request(url=base_url, headers=headers, data=data)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    obj = json.loads(content)
    data = obj['data']
    school_list = data['data']
    for i in school_list:
        conn = Connection(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
            db='graduateschool'
        )
        cursor = conn.cursor()  # 获取到游标对象
        sql = 'insert into school_info(school_id,is_211,type_name,type_school_name,province_area,syl,school_name,clicks,is_985,is_zihuaxian,rk_rank,province_name,is_ads) values(' \
              + str(i['school_id']) + ',' + str(i['is_211']) + ',"' + i['type_name'] + '","' + i[
                  'type_school_name'] + '","' + i['province_area'] + '",' + str(i['syl']) + ',"' + i[
                  'school_name'] + '",' \
              + str(i['clicks']) + ',' + str(i['is_985']) + ',' + str(i['is_zihuaxian']) + ',' + str(
            i['rk_rank']) + ',"' + i['province_name'] + '",' + str(i['is_ads']) + ')'
        print(sql)
        cursor.execute(sql)
        conn.commit()
        conn.close()


def save_sql(i):
    conn = Connection(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        db='graduateschool'
    )
    cursor = conn.cursor()  # 获取到游标对象
    sql = 'insert into school_info(school_id,is_211,type_name,type_school_name,province_area,syl,school_name,clicks,is_985,is_zihuaxian,rk_rank,province_name,is_ads) values(' \
          + str(i['school_id']) + ',' + str(i['is_211']) + ',"' + i['type_name'] + '","' + i[
              'type_school_name'] + '","' + i['province_area'] + '",' + str(i['syl']) + ',"' + i['school_name'] + '",' \
          + str(i['clicks']) + ',' + str(i['is_985']) + ',' + str(i['is_zihuaxian']) + ',' + str(i['rk_rank']) + ',"' + \
          i['province_name'] + '",' + str(i['is_ads']) + ')'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    page = 0;
    end = 107
    for i in range(end):
        page += 1
        requests = create_request(page)
        get_content(requests)
