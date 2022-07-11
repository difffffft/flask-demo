from flask import Blueprint
from router.user_blueprint import bp as user_blueprint

url_prefix = 'api'
bp = Blueprint(url_prefix, __name__, url_prefix=f'/{url_prefix}')
bp.register_blueprint(user_blueprint)


# 校验接口加密
@bp.before_app_request
def verify_sign():
    pass


# 校验用户登录
@bp.before_app_request
def verify_login():
    pass
