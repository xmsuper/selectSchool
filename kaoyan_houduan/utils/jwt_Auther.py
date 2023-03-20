import datetime
import jwt
from jwt import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import logging
salt='iv%x6xo7l7_u9bf_u!9#g#m*)*=ej@bek5)(@u3kh*72+unjv='
def create_token():
    """
    自定义token
    :return:
    """
    # 过期时间
    expire_time=datetime.datetime.utcnow()+datetime.timedelta(days=7)
    # 构造headers,头部
    headers={
        # type属性，标识是jwt
        'typ':'jwt',
        # 算法
        'alg':'HS256'
    }
    # 构造payload，载荷
    payload={
        "userId":1,
        "exp":expire_time
    }
    result=jwt.encode(payload=payload,key=salt,algorithm="HS256",headers=headers).decode('utf-8')
    return result

# 校验token
def parse_payload(token):
    """
    对token进行校验并获取payload
    :param token:
    :return:
    """
    try:
        verified_payload=jwt.decode(token,key=salt)
        return verified_payload
    except jwt.ExpiredSignatureError:
        print('token已失效')
    except jwt.DecodeError:
        print('token认证失败')
    except jwt.InvalidTokenError:
        print("非法的token")


if __name__=='__main__':
    token=create_token()
    print(token)
    print(parse_payload(token))
