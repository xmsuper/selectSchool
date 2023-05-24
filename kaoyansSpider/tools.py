import json
import urllib.request
from pymysql import Connection
url='https://static.kaoyan.cn/json/config/schedule.json'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.1.301'
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
obj=json.loads(content)
data=obj['data']
print(data)

print(data[3])