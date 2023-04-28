# 用于存储Token的功能模块
import jwt
from  django.conf import settings
def create_token(payload):
    salt=settings.SECRET_KEY
    # 构造header
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    jwt_token = jwt.encode(headers=headers, payload=payload, key=salt, algorithm='HS256')

    return jwt_token