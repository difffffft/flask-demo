import jwt
import datetime
from config import TOKEN_SECRET_KEY


def jwt_encrypt(data: dict):
    dic = {
        'exp': datetime.datetime.now() + datetime.timedelta(days=1),  # 过期时间
        'iat': datetime.datetime.now(),  # 开始时间
        'iss': 'lei',  # 签名
        'data': data
    }
    return jwt.encode(dic, TOKEN_SECRET_KEY, algorithm='HS256')


def jwt_decrypt(jwt_str: str):
    return jwt.decode(jwt_str, TOKEN_SECRET_KEY, issuer='lei', algorithms=['HS256'])
