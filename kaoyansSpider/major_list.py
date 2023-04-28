import json
import urllib.request
from pymysql import Connection
# https://api.kaoyan.cn/pc/special/specialList  post
# degree_type: ""
# level1: ""
# level2: ""
# limit: 20
# page: 1
# special_name: ""

def create_request(page):
    base_url = 'https://api.kaoyan.cn/pc/special/specialList'
    data = {
        'page': page,
        'limit': 20,  # 该接口的分页查询是由前端控制的，所以这里直接设置一个很大的值
        'level1': '',
        'level2': '',
        'degree_type': '',
        'special_name': ''
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
    major_list = data['data']
    for i in major_list:
        # i['special_name']=i['special_name'].replace('"',"'")
        # i['degree_name']=i['degree_name'].replace('"',"'")
        # i['degree_name']=i['degree_name'].replace('"',"'")
        # i['degree_name']=i['degree_name'].replace('"',"'")
        conn = Connection(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
            db='graduateschool'
        )
        cursor=conn.cursor()
        sql='insert into major(major_code,spe_id,major_name,major_class,level1_name,level2_name) values ("'+str(i['code'])+'",'+str(i['spe_id'])+',"'+i['special_name']+'","'+i['degree_name']+'","'+i['level1_name']+'","'+i['level2_name']+'")'
        print(sql)
        cursor.execute(sql)
        conn.commit()
        conn.close()

if __name__=='__main__':
    page=0;
    end=122
    for i in range(end):
        page+=1
        print('正在插入第'+str(i)+'页数据')
        requests=create_request(page)
        get_content(requests)
        print('插入成功')