from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pymysql import Connection

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    # path是你自己浏览器的路径
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser
browser = share_browser()
url = 'http://www.chinakaoyan.com/info/article/id/318459.shtml'
browser.get(url)
result=browser.find_elements(By.XPATH,"//div[@class='cont'][2]/p")
test_tiku=[]
for k,v in enumerate(result):
    if (v.text).startswith('三、材料分析题'):
        break
    else:
        if (v.text).startswith(('一、单选题','二、多项选择题')):
            continue
        else:
            if len((v.text.split(' ')))>3:
                for i in (v.text.split(' ')):
                    print(i)
                    test_tiku.append(i)
            else:
                test_tiku.append(v.text)


tiku=[]
for i in range(0,len(test_tiku),7):
    tiku.append(test_tiku[i:i+7])
# print(tiku)
for i in tiku:
    print(i)
    conn = Connection(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        db='graduateschool'
    )
    sql ='insert into zhengzhitiku(subject,optionsA,optionsB,optionsC,optionsD,answer,explation) ' \
         'values("'+i[0]+'","'+i[1]+'","'+i[2]+'","'+i[3]+'","'+i[4]+'","'+i[5]+'","'+i[6]+'")'
    print(sql)
    cursor = conn.cursor()  # 获取到游标对象
    cursor.execute(sql)
    conn.commit()
    conn.close()


    # if i.text.startswith('一、单选题') or i.text.startswith('二、多选题'):
    #     print(i.text)
    # else:
    #     test_tiku.append(i.text)
# print(test_tiku)





# if __name__=='__main__':
#     share_browser()