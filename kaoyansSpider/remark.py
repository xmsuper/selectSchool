import json
import urllib.request
from pymysql import Connection


conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    db='graduateschool'
)
cursor = conn.cursor()  # 获取到游标对象
sql = "select distinct s.school_id,s.school_name,s.province_name,s.rk_rank,s.major_name,s.learnType,left(s.total,3),m.recruit_type,s.major_code,m.recruit_number from (select a.school_id,a.school_name,a.rk_rank,a.province_name,b.learnType,b.major_name,b.total,b.major_code from school_info a left join school_score b on a.school_name=b.school_name) s left join major_detail m on s.school_name=m.school_name and s.school_id=m.school_id and s.major_code=m.special_code"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
# cursor.close()
# conn.close()

for v,k in enumerate((results)):
    print(k[0],k[4])
    score=0
    print(k[0])
    major_name=k[4]
    if major_name==None:
        major_name=''
    if k[3]<10:
        score+=10
    elif k[3]<50:
        score+=8;
    elif k[3]<100:
        score+=5
    elif k[3]<200:
        score+=3
    elif k[3]<500:
        score+=1
    else:
        score+=0

    if k[6]:
        if int(k[6][0:3])<200:
            score+=20
        elif int(k[6][0:3])<270:
            score+=15
        elif int(k[6][0:3])<300:
            score+=10
        elif int(k[6][0:3])<320:
            score+=8
        elif int(k[6][0:3])<350:
            score+=6
        elif int(k[6][0:3])<380:
            score+=4
        elif int(k[6][0:3])<400:
            score+=2
        elif int(k[6][0:3])<420:
            score+=1
        else:
            score+=0
    if k[6]==None:
        total=0
    else:
        total=k[6][0:3]

    recruit_number=k[9]
    if k[9]==None:
        recruit_number=0
    if k[9]:
        if k[9]<5:
            score+=1
        elif k[9]<10:
            score+=5
        elif k[9]<20:
            score+=10
        elif k[9]<50:
            score+=15
        elif k[9]<100:
            score+=20
        else:
            score+=30


    sql='insert into school_remark(school_id,school_name,major_name,school_rank,score,major_code,recruit_num,remark) values('+str(k[0])+',"'+k[1]+'","'+major_name+'",'+str(k[3])+','+str(total)+',"'+str(k[8])+'",'+str(recruit_number)+','+str(score)+');'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    # conn.close()
    print('插入成功')
    score=0
cursor.close()
conn.close()


