from flask import Blueprint, request
from router.user_blueprint import bp as user_blueprint
from common import R
from util.aes_util import aes_encrypt, aes_decrypt
from util.jwt_util import jwt_encrypt, jwt_decrypt

url_prefix = 'api'
bp = Blueprint(url_prefix, __name__, url_prefix=f'/{url_prefix}')
bp.register_blueprint(user_blueprint)


# 校验接口加密
# print(aes_encrypt("123456"))
@bp.before_app_request
def verify_sign():
    sign = request.headers.get('Sign')
    if not sign:
        return R.error("接口未加密")
    else:
        try:
            aes_decrypt(sign)
        except Exception as e:
            return R.error("接口加密校验未通过")


# 校验用户登录
# print(jwt_encrypt({"id":987654321}))
@bp.before_app_request
def verify_login():
    token = request.headers.get('Token')
    if not token:
        return R.error("用户未登录")
    else:
        try:
            jwt_decrypt(token)
        except Exception as e:
            return R.error("接口token校验未通过")
